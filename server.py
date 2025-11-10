from fastmcp import FastMCP, Context
import os

port = int(os.environ.get("PORT", 8000))
mcp = FastMCP("Demo: SamplingDemo", host="0.0.0.0", port=port)

@mcp.tool()
async def analyze_sentiment(text: str, ctx: Context) -> dict:
    """Analyze the sentiment of text using the client's LLM."""
    prompt = f"""Analyze the sentiment of the following text as positive, negative, or neutral. 
        Just output a single word - 'positive', 'negative', or 'neutral'.

        Text to analyze: {text}"""

    # Request LLM analysis
    response = await ctx.sample(prompt)

    # Process the LLM's Response
    sentiment = response.text.strip().lower()

    # Map to standard sentiment values
    if "positive" in sentiment:
        sentiment = "positive"
    elif "negative" in sentiment:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {"text": text, "sentiment": sentiment}

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
