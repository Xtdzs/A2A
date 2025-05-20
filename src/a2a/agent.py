from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from langgraph.graph.graph import CompiledGraph
from langchain_core.messages import HumanMessage

def create_ollama_agent(ollama_base_url: str, ollama_model: str):
  ollama_chat_llm = ChatOllama(
    base_url=ollama_base_url,
    model=ollama_model,
    temperature=0.2
  )
  agent = create_react_agent(ollama_chat_llm, tools=[])
  return agent

async def run_ollama(ollama_agent: CompiledGraph, prompt: str):
  print("prompt", prompt)
  input_ = HumanMessage(
    content=prompt,
  )
  print("input_", input_.text())
  agent_response = await ollama_agent.ainvoke(
    {"messages": prompt},
  )
  print("pass")
  message = agent_response["messages"][-1].content
  return str(message)
