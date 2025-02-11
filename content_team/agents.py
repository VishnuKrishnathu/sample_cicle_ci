from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv

load_dotenv()


class ContentTeam:
    def __init__(self):
        self.writer = Agent(
            role='Senior Content Writer',
            goal='Create engaging blog posts about AI trends',
            backstory="""An experienced writer specialized in technology 
                       and AI content. Known for making complex topics 
                       accessible and interesting.""",
            verbose=True,
            llm=os.getenv('OPENAI_MODEL', 'openai/gpt-4')
        )

        self.editor = Agent(
            role='Editor',
            goal='Ensure content quality and accuracy',
            backstory="""A meticulous editor with expertise in technical 
                      content. Focuses on clarity, grammar, and factual 
                      accuracy.""",
            verbose=True,
            llm=os.getenv('OPENAI_MODEL', 'openai/gpt-4')
        )

    def create_post(self, topic):
        write_task = Task(
            description=f"""Write a comprehensive blog post about {topic}.
                          Focus on recent developments and practical 
                          applications. Minimum 500 words.""",
            agent=self.writer,
            expected_output='Formatted markdown content with headings'
        )

        edit_task = Task(
            description="""Review the blog post for errors, improve clarity, 
                         and ensure proper formatting.""",
            agent=self.editor,
            expected_output='Polished markdown content ready for publication'
        )

        crew = Crew(
            agents=[self.writer, self.editor],
            tasks=[write_task, edit_task],
            verbose=True
        )

        return crew.kickoff().raw


if __name__ == "__main__":
    team = ContentTeam()
    result = team.create_post("Large Language Models in Healthcare")
    print("\n\nFinal Content:")
    print(result)
