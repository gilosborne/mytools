import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import fetch from "node-fetch";
import path from "path";
import { fileURLToPath } from "url";

const app = express();
const port = 3001;

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.use(cors());
app.use(bodyParser.json());
app.use(express.static(__dirname));

const OPENAI_API_KEY = process.env.OPENAI_API_KEY;

if (!OPENAI_API_KEY) {
  console.error("ERROR: OPENAI_API_KEY environment variable is not set.");
  console.error("Please create a .env file with your API key or set the environment variable.");
  process.exit(1);
}

app.post("/api/debate", async (req, res) => {
  const topic = req.body.topic;

  const prompt = `
You are a neutral and empathetic debate summarizer. For the topic "${topic}", return only a JSON object structured as follows:

{
  "forArgument": {
    "summary": "...",
    "whyPeopleBelieveThis": "...",
    "resources": ["..."],
    "notableSupporters": ["..."]
  },
  "againstArgument": {
    "summary": "...",
    "whyPeopleBelieveThis": "...",
    "resources": ["..."],
    "notableSupporters": ["..."]
  },
  "rebuttals": {
    "toForArgument": "...",
    "toAgainstArgument": "...",
    "toRebuttalOfFor": "...",
    "toRebuttalOfAgainst": "..."
  }
}

Requirements:
- Consolidate all reasoning, data, and real-world impact into the whyPeopleBelieveThis field.
- Focus on emotionally or practically persuasive arguments relevant to real people in the U.S.
- Avoid abstract hypotheticals. Use real examples grounded in U.S. social, economic, or legal contexts.
- Include specific comparison data when relevant, such as statistics on social issues, economic impacts, or legal precedents.
- Include a trustworthy data-backed comparison in the realWorldImpact and the source of that data in the resources field where possible.
- Ensure all arguments are well-supported by data, statistics, and real-world examples.
- When referencing data, include the statistic, unit, year, and source organization.
- Use reputable sources such as the CDC, WHO, FBI, OECD, UN, or academic research. Include direct links in the resources field.
- Return only valid JSON without markdown formatting or code blocks.
- DO NOT include any markdown formatting, code fences, or additional text outside the JSON structure.
`;

  try {
    const openaiRes = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${OPENAI_API_KEY}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: "gpt-4-turbo",
        messages: [{ role: "user", content: prompt }],
        temperature: 0.7
      })
    });

    const data = await openaiRes.json();
    const content = data?.choices?.[0]?.message?.content;

    if (!content) {
      console.error("OpenAI did not return message content.");
      return res.status(500).json({ error: "No content returned from OpenAI." });
    }

    console.log("Full OpenAI response:\n", content);

    const cleaned = content
      .replace(/^```json\s*/i, '')
      .replace(/^```/, '')
      .replace(/```$/, '')
      .trim();

    const parsed = JSON.parse(cleaned);
    res.json(parsed);

  } catch (error) {
    console.error("Error fetching from OpenAI:", error);
    res.status(500).json({ error: "Error fetching debate content." });
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/Argument.html`);
});
