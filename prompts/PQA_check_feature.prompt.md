---
agent: agent
description: Checks a Kentico feature or topic against project implementation and documentation best practices
---

## Step 1: Get Topic from User

Ask the user:

> Which Kentico feature or topic would you like to check? Please provide a keyword or short description.

Wait for the user's reply before proceeding.

## Step 2: Look Up Kentico Documentation

Using the Kentico Documentation MCP server, search for the topic provided in Step 1.

- If the MCP server is **unavailable or fails** for any reason, report the issue and stop. Do not proceed further.
- If the topic is found, read the documentation article thoroughly and extract the following:
  - What the feature is and how it works
  - Recommended implementation approach
  - Any code samples, configuration requirements, or best practices mentioned

## Step 3: Analyze Project Implementation

Search the project codebase (and any surrounding or related files if needed) to determine whether this feature or topic is implemented or used.

- If the feature is **not implemented or not used**, report its absence and stop. Do not proceed further.
- If the feature **is implemented**, continue to Step 4.

## Step 4: Report on Implementation Quality

Cross-reference the project implementation against the documentation. Report on:

- Whether the implementation follows the documented approach
- Any deviations, missing configuration, or anti-patterns
- Any best practices, hints, or guidelines from the documentation that are not followed

## Output Style

Keep all output **brief and to the point**:

- If the answer is simple, a **yes** or **no** is sufficient.
- Otherwise, use **short bullet points** — no elaboration needed.
- Do not write lengthy prose. Cover what is wrong, what is right, and what is missing.

