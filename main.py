import google.generativeai as genai

# Set up your Gemini API key
genai.configure(api_key='AIzaSyCBEeXkoWxMOICddo6T5PO9u3LRkkmHTPU')

# Define the model
model = genai.GenerativeModel('gemini-2.0-flash')

def verify_correctness(question, student_answer):
    """
    Step 1: Verify if the student's answer is factually correct using Gemini's web access.
    """
    prompt = f"""
    Question: {question}
    Student Answer: {student_answer}

    Using web access, verify if the student's answer is factually correct for the given question.
    Provide a response in the following format:
    - Correctness: True/False
    - Explanation: Brief explanation of why the answer is correct or incorrect.
    """
    response = model.generate_content(prompt)
    return response.text

def match_desired_answer(correct_answer, student_answer):
    """
    Step 2: Compare the student's answer with the desired answer on a scale of 1 to 5.
    """
    prompt = f"""
    Correct Answer: {correct_answer}
    Student Answer: {student_answer}

    Compare the student's answer with the desired answer based on meaning, depth, and relevance.
    Provide a grade between 1 and 5, where:
    - 1: The answer is completely incorrect or irrelevant.
    - 2: The answer is partially correct but lacks significant meaning or relevance.
    - 3: The answer is somewhat correct but has minor inaccuracies or omissions.
    - 4: The answer is mostly correct and conveys the meaning well.
    - 5: The answer is fully correct and perfectly matches the meaning of the correct answer.

    Also, provide a brief explanation for the grade.
    """
    response = model.generate_content(prompt)
    return response.text

def evaluate_answer(question, correct_answer, student_answer):
    """
    Main function to evaluate the student's answer.
    """
    # Step 1: Verify correctness
    correctness_response = verify_correctness(question, student_answer)
    print("Correctness Verification:")
    print(correctness_response)

    # Extract correctness from the response
    if "Correctness: True" in correctness_response:
        print("The student's answer is factually correct. Proceeding to match with the desired answer.")
        # Step 2: Match with desired answer
        match_response = match_desired_answer(correct_answer, student_answer)
        print("\nDesired Answer Matching:")
        print(match_response)
    else:
        print("The student's answer is factually incorrect. No further evaluation needed.")

# Example 1: Complex question with similar meaning but different structure
question1 = "Explain the significance of the Industrial Revolution in shaping modern society."
correct_answer1 = "The Industrial Revolution was a pivotal period in history that transformed societies from agrarian economies to industrialized ones. It introduced technological advancements, urbanization, and significant social changes, laying the foundation for modern society."
student_answer1 = "The Industrial Revolution played a crucial role in modernizing society by shifting economies from agriculture to industry. It brought about technological innovations, urban growth, and social transformations that shaped the world we live in today."

# Example 2: Complex question with similar meaning but different structure
question2 = "Discuss the impact of climate change on global ecosystems."
correct_answer2 = "Climate change has profound effects on global ecosystems, including rising temperatures, melting ice caps, and altered weather patterns. These changes disrupt habitats, threaten biodiversity, and impact the survival of many species."
student_answer2 = "Global ecosystems are significantly affected by climate change, which causes higher temperatures, shrinking ice caps, and unpredictable weather. These disruptions endanger biodiversity and challenge the survival of numerous species."

# Example 3: Complex question with similar meaning but different structure
question3 = "What are the key factors that contribute to economic growth in developing countries?"
correct_answer3 = "Economic growth in developing countries is driven by factors such as investment in infrastructure, education, technological adoption, and stable governance. These elements create an environment conducive to productivity and innovation."
student_answer3 = "Fuck you examiniatopn."

# Evaluate the answers
print("Evaluating Example 1:")
evaluate_answer(question1, correct_answer1, student_answer1)

print("\nEvaluating Example 2:")
evaluate_answer(question2, correct_answer2, student_answer2)

print("\nEvaluating Example 3:")
evaluate_answer(question3, correct_answer3, student_answer3)