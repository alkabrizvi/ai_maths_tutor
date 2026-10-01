from backend.ai.schemas import TutorRequest
from backend.ai.tutor import generate_tutor_response


def main():
    print("=== AI Maths Tutor ===")
    print("Type 'exit' to stop.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            print("Please enter a question.\n")
            continue

        request = TutorRequest(
    question=question,
    student_level="beginner",
    explanation_style="simple",
    language="hinglish",
)
        response = generate_tutor_response(request)

        print("\nTutor:")
        print(response.answer)

        if response.error:
            print("\nError:", response.error)

        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()