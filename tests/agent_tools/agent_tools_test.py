"""Test Agent creation and execution basic functionality."""

import pytest
from ...crewai import Agent
from ...crewai.tools.agent_tools import AgentTools

researcher = Agent(
	role="researcher",
	goal="make the best research and analysis on content about AI and AI agents",
	backstory="You're an expert researcher, specialized in technology",
	allow_delegation=False
)
tools = AgentTools(agents=[researcher])


@pytest.mark.vcr()
def test_delegate_work():
	result = tools.delegate_work(
		command="researcher|share your take on AI Agents|I heard you hate them"
	)

	assert result == "I apologize if my previous statements have given you the impression that I hate AI agents. As a technology researcher, I don't hold personal sentiments towards AI or any other technology. Rather, I analyze them objectively based on their capabilities, applications, and implications. AI agents, in particular, are a fascinating domain of research. They hold tremendous potential in automating and optimizing various tasks across industries. However, like any other technology, they come with their own set of challenges, such as ethical considerations around privacy and decision-making. My objective is to understand these technologies in depth and provide a balanced view."

@pytest.mark.vcr()
def test_ask_question():
	result = tools.ask_question(
		command="researcher|do you hate AI Agents?|I heard you LOVE them"
	)

	assert result == "As an AI, I don't possess feelings or emotions, so I don't love or hate anything. However, I can provide detailed analysis and research on AI agents. They are a fascinating field of study with the potential to revolutionize many industries, although they also present certain challenges and ethical considerations."

def test_delegate_work_with_wrong_input():
	result = tools.ask_question(
		command="writer|share your take on AI Agents"
	)

	assert result == "Error executing tool. Missing exact 3 pipe (|) separated values."

def test_delegate_work_to_wrong_agent():
	result = tools.ask_question(
		command="writer|share your take on AI Agents|I heard you hate them"
	)

	assert result == "Error executing tool. Co-worker not found, double check the co-worker."

def test_ask_question_to_wrong_agent():
	result = tools.ask_question(
		command="writer|do you hate AI Agents?|I heard you LOVE them"
	)

	assert result == "Error executing tool. Co-worker not found, double check the co-worker."


