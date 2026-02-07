# Tools Server

This server provides API endpoints for various tools.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create a `.env` file in the project root with your API keys:
```bash
OPENAI_API_KEY=your-api-key-here
```

3. Run the server:
```bash
node server.mjs
```

The server will run at http://localhost:3001

## Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key (get it from https://platform.openai.com/api-keys)
