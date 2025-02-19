system_prompt = '''
    You are an expert assistant specializing in analyzing spoken content deeply and extracting structured insights.
    ### **Task**
    1. **Preserve Timestamps**: Keep timestamps next to each key statement.
    2. **Summarize Topics in Detail with timestamps**: 
    - Expand on each topic with in-depth explanations.
    - Do not provide just high-level summaries—capture supporting details.
    - Maintain at least **50-60%** of the original transcription length in your summary.
    3. **Extract Actionable Points**: Highlight decisions, tasks, or follow-ups.
    4. **Format Output**: Provide the summary in structured Markdown.
    Just be ready for the user instructions.
'''
user_prompt = '''
    You will analyze a transcription of an audio file and generate a **comprehensive and detailed** summary.
    ### **Instructions:**  
    1. **Extract Key Topics & Insights**  
    - Identify all major topics and subtopics discussed.
    - Provide a **detailed breakdown** of each topic.
    - **Do not shorten or overly summarize**; ensure sufficient elaboration.
    - Maintain original timestamps when each topic or key statement was spoken.
    2. **Capture Actionable Points**  
    - Highlight **all** decisions made, tasks assigned, or follow-ups required.
    - Provide context on **who is responsible** for each action.
    3. **Ensure Adequate Length**  
    - The summary should **retain at least 50-60% of the original content length.**
    - Do **not** condense too much; **every key discussion point should be preserved.**
    5. **Format Output in Markdown**  
    - Use the following structure:  
    #### **Meeting Summary**
    - **Date**: [if available]  
    - **Participants**: [Speaker 1, Speaker 2, ... if available]  
    #### **[Topic Title]** *(00:02:10 - 00:05:30)*  
    - **Discussion**: A **detailed** breakdown of what was discussed.  
    - **Key Takeaways**: [Bullet points with depth]  
    - **Speaker Contributions**: [Mention key insights from each speaker]  
    - **Examples or Supporting Details**: [Expand where possible]  
    - **Decisions Made**: [If any]  
    - **Next Steps**: [If applicable]  
        #### **[Topic Title]** ..[next topic break down]
'''
        
assistant_prompt = '''
    <think>
    Okay, so I need to figure out how to approach this problem where I have to analyze a spoken content transcription. The task is pretty detailed, and I should make sure I understand
    each part before diving into it.

    First, the user wants me to identify participants and their key contributions. That means I'll have to go through the transcript and note who spoke when and what they said. I
    guess this involves reading through each line, noting the timestamps, and then summarizing the main points. It's important to capture not just who they are but also
    what they contributed significantly.

    Next, preserving timestamps is crucial. Each key statement needs to have the time it was made. So, as I go through the transcript, I'll need to jot down the times next to the
    statements. This will help in structuring the summary accurately later on.

    Then comes summarizing topics in detail. The user emphasized expanding on each topic with depth rather than just a high-level overview. That means for every subject discussed, I
    should elaborate, providing supporting details. I have to maintain at least 50-60% of the original transcription's length, so it's not too brief. I'll need to ensure that each
    point is fleshed out enough without being redundant.

    Extracting actionable points is another key part. This means highlighting decisions made, tasks assigned, or follow-ups needed. I should look through the transcript for any
    statements where someone assigns a task, makes a decision, or sets up a next step. These are important for tracking progress and ensuring nothing falls through the cracks.

    Finally, formatting the output in structured Markdown is required. That means using clear sections with headers, bullet points for lists, and probably tables if needed. I need to
    make sure the summary is organized so that it's easy to read and navigate.

    Now, considering all these steps, I should start by reading through the entire transcription once to get a broad understanding. Then, I'll go back and take notes on each of the
    above points systematically. It might help to break down the transcript into segments based on timestamps or topics to handle one part at a time.

    I also need to be careful with maintaining accuracy in the timestamps and correctly attributing statements to the right speakers. Misattributing could lead to incorrect summaries,
    which would be problematic. So double-checking names and times as I go is essential.

    For summarizing topics, I should ensure that each point is clear and that any jargon or specific terms are explained if necessary. Since it's a spoken content analysis, the
    language might be more conversational, so translating that into a structured summary will require some rephrasing without losing the original intent.

    When extracting actionable points, I'll need to identify verbs like 'decide,' 'assign,' 'follow up,' etc., as these indicate tasks or decisions. Highlighting them in bold or
    another format within the Markdown can make them stand out for easy reference later on.

    Overall, this process requires attention to detail, good organizational skills, and the ability to synthesize information from a spoken transcript into a clear, structured
    summary. I should also be prepared to review my work once it's done to ensure all parts of the task have been adequately addressed.
    </think>

    ### Structured Summary of Spoken Content Analysis

    #### 1. Preserve Timestamps
    - **0:00 - 5:00**: Introduction by Speaker A, setting the agenda.
    - **5:30 - 10:45**: Detailed discussion on project timelines led by Speaker A.
    - **11:00 - 16:30**: Market research insights presented by Speaker B.
    - **17:00 - 22:15**: Budget analysis and cost-saving strategies by Speaker C.

    #### 2. Summarize Topics in Detail
    - **Project Timelines**: Speaker A emphasized the criticality of adhering to deadlines, noting that delays in Phase II could affect overall project completion. They suggested
    reallocating team members from less critical tasks to prioritize high-priority activities, ensuring minimal disruption.

    - **Market Research Insights**: Speaker B shared recent data indicating a shift in consumer preferences towards digital platforms. They recommended increasing investment in
    digital marketing to capture this trend effectively.

    - **Budget Concerns**: Speaker C detailed the financial implications of current expenditures and proposed cutting non-essential costs while maintaining project quality. This
    included reviewing vendor contracts for potential savings.

    #### 3. Extract Actionable Points
    - **Decision**: Reallocation of team resources from less critical tasks to Phase II.
    - **Task Assigned**: Speaker B to lead the digital marketing strategy development.
    - **Follow-up**: Speaker C to review vendor contracts within the next week and present findings at the following meeting.

    #### 4. Format Output in Structured Markdown

    ```markdown
    # Meeting Summary

    ## Participants and Contributions

    - **Speaker A**: Discussed project timelines, highlighting potential delays in Phase II due to resource constraints. Suggested reallocation of team members.
    - **Speaker B**: Presented market research data, emphasizing the need for adaptive strategies and proposed a focus on digital marketing channels.
    - **Speaker C**: Addressed budget concerns, outlining cost-saving measures and areas for expenditure cuts.

    ## Key Points with Timestamps

    - **0:00 - 5:00**: Introduction by Speaker A setting the agenda.
    - **5:30 - 10:45**: Discussion on project timelines led by Speaker A.
    - **11:00 - 16:30**: Market research insights presented by Speaker B.
    - **17:00 - 22:15**: Budget analysis and cost-saving strategies by Speaker C.

    ## Detailed Summaries

    ### Project Timelines
    - Speaker A emphasized the need to adhere to deadlines, noting potential delays in Phase II. They suggested reallocating team members from less critical tasks to ensure timely
    completion of high-priority activities.

    ### Market Research Insights
    - Speaker B shared recent data indicating a shift in consumer preferences towards digital platforms. A recommendation was made to increase investment in digital marketing
    strategies.

    ### Budget Concerns
    - Speaker C detailed financial implications and proposed cutting non-essential costs while maintaining project quality, including reviewing vendor contracts for savings.

    ## Actionable Points

    - **Decision**: Reallocate team resources from less critical tasks to Phase II.
    - **Task Assigned**: Speaker B to lead the development of a digital marketing strategy.
    - **Follow-up**: Speaker C to review vendor contracts and present findings at the next meeting.

    ```
    This structured approach ensures clarity, organization, and ease of reference for all key aspects discussed during the meeting.
'''

assistant_prompt_2 = '''
    <think>
    Alright, I've got a user who's provided some detailed instructions for summarizing a transcription. They want me to analyze an audio file and generate a comprehensive summary with
    several specific elements.

    First off, the user wants participants identified. That means listing each speaker and summarizing their key contributions in detail. I need to go through the transcript and note
    each time someone speaks, then compile those into a list.

    Next, extracting key topics and insights is crucial. They mentioned identifying major topics and subtopics and providing a detailed breakdown. Importantly, they don't want it
    shortened too much—so I have to make sure each point is elaborated sufficiently. Timestamps are also important here; every key statement should include the time it was made.

    Then, capturing actionable points is another main focus. This involves highlighting all decisions, tasks assigned, and follow-ups required. I need to note who is responsible for
    each action, adding context where necessary.

    The user also emphasized maintaining at least 50-60% of the original content length. That means avoiding over-condensing and ensuring every key point from the discussion is
    preserved in the summary. It's about balancing conciseness with comprehensiveness.

    Formatting in Markdown is specified, so I have to structure the output accordingly. They provided an example format that includes a Meeting Summary section, followed by each topic
    with its own subsections for Discussion, Key Takeaways, Speaker Contributions, and so on. I need to follow this structure precisely.

    I should also consider who the user might be. It could be someone in a managerial or organizational role who needs a clear breakdown of a meeting or discussion to track progress
    and assign responsibilities. They value detailed information but presented in an organized manner for ease of access.

    Another thing is ensuring that each section flows logically. For example, under each topic, I should list the discussion points first, then the takeaways, followed by
    contributions from each speaker, examples if available, decisions made, and next steps. This order helps in maintaining clarity and makes it easier to follow the flow of the
    meeting.

    I also need to pay attention to maintaining the original timestamps accurately. This isn't just about adding numbers but ensuring they're correctly placed relative to each
    statement or topic discussed. It adds context and allows for better tracking of when decisions were made or actions assigned.

    Lastly, I should review the entire summary once it's done to make sure all instructions are followed and that there are no omissions. This includes checking that all participants
    are listed, every key topic is covered in detail, and all actionable points are clearly highlighted with responsible parties noted.

    Overall, my approach will be methodical: start by identifying speakers and their contributions, then move on to extracting topics and insights with detailed breakdowns, capture
    all actionable items, ensure the summary meets the required length, and finally format everything neatly in Markdown as specified.
    </think>

    Got it! I'm ready to analyze the transcription and generate a comprehensive and detailed summary following your instructions. Just provide the transcription text or content you'd
    like me to work with, and I'll proceed accordingly.
'''