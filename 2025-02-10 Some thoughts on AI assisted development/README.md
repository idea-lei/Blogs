# Some thoughts on AI assisted development

**Disclaimer**: This article was written in early 2025. Given the rapid advancement of AI technology, the views expressed here may become outdated or prove inaccurate in the future. Readers are advised to interpret and evaluate the content in light of current conditions.

## Foreword

This article uses a software development project as an example to demonstrate how AI can be applied to conceptual design and code implementation. It also shares what I consider best practices, which can be extended to other types of complex problems.

At present, AI-assisted programming generally takes two forms:

1. **Q&A-Based Approach**: Interacting with general-purpose Large Language Models (LLMs), such as ChatGPT or DeepSeek, by asking questions and then integrating the generated insights or code into your project.
2. **AI Integrated into the IDE**: Using plugins or extensions like GitHub Copilot or Cursor so that the AI can directly participate in writing and modifying code.

From a functional and strategic perspective, general-purpose LLMs are better suited for high-level conceptual work, strategic planning, and idea validation in the early stages; meanwhile, IDE-integrated AI is more adept at concrete, repetitive tasks at the tactical level. Obviously the LLMs with deep thinking support will offer deeper reasoning and better handling of complex requirements.

The primary focus of this article is on how to leverage AI for conceptual work, such as defining a project’s system architecture or overall solution. The underlying principle is still to “break down big problems into smaller ones” while clearly expressing your thoughts: on the one hand, you deepen your understanding of the project; on the other hand, you provide the LLM with sufficient context to deliver higher-quality recommendations.

## Action Steps

1. **Clarify Requirements**

   To start, clearly define your current primary goals while leaving room for potential future adjustments. It is recommended to adopt DDD (Domain-Driven Design) or a top-down approach commonly used in engineering. Only when you can accurately articulate your needs can an LLM provide results that closely match your expectations. Although requirements may evolve, it’s crucial to specify the key objectives for each stage.

2. **Use “Comprehensive Descriptions,” Not “One-Line Chats”**

   When devising solutions with an LLM, one of the biggest pitfalls is providing only one or two sentences as a prompt. Doing so forces the model to make many assumptions—some of which may clash with your unstated requirements—leading to inaccurate results. Think of it more like writing an “email” rather than sending “chat messages.” A thorough prompt should include requirements, background, constraints, and even your initial ideas all at once. This significantly improves the LLM’s understanding of your context.
   If you’re unsure how to structure your prompt, you can first ask the LLM for help in organizing or refining your requirements, then consolidate that information into a more systematic prompt for it to analyze. A prompt wizard would definitely help.

3. **Summarize and Restart Prompting When Needed**

   If discussions lead to evolving requirements or if the conversation becomes unwieldy after too many exchanges, consider having the AI summarize the key points so far. Use this summary as the foundation of a new dialogue. This approach prevents an excessive “patch-up” style of conversation and helps maintain conceptual clarity, reducing both misinformation and confusion.

4. **Build a Demo and Validate**

   Once the AI provides an outline or solution, start with a small-scale Demo or prototype. Test the core logic to ensure it’s viable before integrating AI-generated outputs into a live project. This helps you catch potential issues early and avoid committing unverified AI suggestions to production code.

5. **Learn and Improve**

   AI-generated answers often introduce novel concepts, tools, or methodologies. Seize this opportunity to expand your knowledge base and skill set. By continuously engaging with AI and absorbing new information, you broaden your perspective and reinforce your professional abilities.

## Additional Perspectives

1. **Impact on Developers**
   While AI may replace or reduce the need for some junior-level tasks, individuals with solid experience and a commitment to ongoing learning can treat AI as a productivity multiplier. Senior developers with a strong technical foundation can craft higher-quality prompts and gain even more from AI assistance. On the other hand, those who stop learning and merely copy and paste AI outputs risk losing relevance in the market.
   Here, “Junior” does not strictly refer to someone young or with fewer years of experience, but rather to anyone who remains rigid and fails to adapt to or utilize new technologies in a timely manner.
2. **The Importance of Continuous Learning**
   In the AI era, “learning” remains a key factor in differentiating individuals’ capabilities. The difference is that learning must be more targeted and strategic. Knowing what to learn and how to learn fundamentally tests one’s cognitive flexibility and adaptability.
3. **Potential Evolution of Future Work**
   From a more radical standpoint, in ten years or so, those who retain strong value in the workplace might be those with broad vision and creativity, or those with deep expertise in solving very challenging problems. Both groups would rely heavily on AI to boost productivity. That said, the future of work may become more diverse, and having both breadth and depth of knowledge could be mutually reinforcing rather than mutually exclusive.