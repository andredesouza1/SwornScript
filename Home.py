import streamlit as st



image_path = "SwornScriptLogo.jpg"

st.image(image_path,width=100,)

st.title("Sworn Script")

st.write("""A pressing challenge faced by many legal entities such as law firms, courts, and law enforcement agencies is the efficient processing of lengthy written documents, often resulting in backlogs that lead to case delays. Furthermore, the arduous task of sifting through extensive documents to uncover pertinent information is exacerbated by the need to wade through superfluous content.

Enter Sworn Script, a cutting-edge document management and review system powered by OpenAI and the lightweight AI engineering framework, Marvin. Sworn Script offers a powerful solution to these challenges by harnessing Marvin's suite of tools to swiftly and effectively extract relevant data from large documents.

Marvin employs Pydantic BaseModels in tandem with specialized decorators, facilitating the creation of unique and functional outcomes. Leveraging Pydantic's data validation and serialization capabilities, Marvin simplifies the development process. The integration of AI Models (@ai_models) enables structured data extraction from unstructured text, documents, or instructions, all while imposing a rigid output structure. With AI Functions (@ai_fn), developers can craft custom functions that leverage the generative and non-deterministic attributes of LLMs while maintaining output consistency within defined types. Lastly, AI Classifiers(@ai_classifier) employ a clever logit bias technique to guide an LLM in deducing the optimal output.

Collectively, these tools yield outputs that are notably superior to direct querying of the LLM. Anyone familiar with experimenting with LLMs understands the frustration of achieving specific output structures, and these tools significantly enhance result consistency.

Powered by Marvin, Sworn Script efficiently extracts data from GPT-3.5-Turbo, unlocking a realm of possibilities for the development of diverse applications. Sworn Script is poised to revolutionize the realm of LawTech and has the potential for application in various other domains.""")