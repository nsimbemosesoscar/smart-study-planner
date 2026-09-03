# Smart Study Planner
# Programming Fundamentals Coursework

sessions = []


# (c) Classify the study session according to duration
def classify_session(duration):
    if duration < 30:
        return "Short"
    elif duration <= 90:
        return "Medium"
    else:
        return "Long"


# (b) Add a new study session
def add_session():
    print("\n===== ADD STUDY SESSION =====")

    subject = input("Enter subject name: ")
    topic = input("Enter topic covered: ")
    date = input("Enter date or day: ")

    while True:
        try:
            duration = float(input("Enter duration in minutes: "))

            if duration > 0:
                break
            else:
                print("Duration must be a positive number.")

        except ValueError:
            print("Please enter a valid number.")

    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration
    }

    sessions.append(session)

    print("Study session added successfully.")


# (d) View all study sessions
def view_sessions():
    if not sessions:
        print("\nNo study sessions have been recorded.")
        return

    print("\n================ ALL STUDY SESSIONS ================")
    print(f"{'Subject':<20}{'Topic':<25}{'Duration':<12}{'Class':<10}")
    print("-" * 67)

    for session in sessions:
        classification = classify_session(session["duration"])

        print(
            f"{session['subject']:<20}"
            f"{session['topic']:<25}"
            f"{session['duration']:<12.1f}"
            f"{classification:<10}"
        )


# (e) Search sessions by subject
def search_by_subject(subject):
    found_sessions = []
    total_time = 0

    for session in sessions:
        if session["subject"].lower() == subject.lower():
            found_sessions.append(session)
            total_time += session["duration"]

    if not found_sessions:
        print("\nNo sessions found for that subject.")
        return

    print(f"\n========== SESSIONS FOR {subject} ==========")
    print(f"{'Subject':<20}{'Topic':<25}{'Duration':<12}{'Class':<10}")
    print("-" * 67)

    for session in found_sessions:
        classification = classify_session(session["duration"])

        print(
            f"{session['subject']:<20}"
            f"{session['topic']:<25}"
            f"{session['duration']:<12.1f}"
            f"{classification:<10}"
        )

    print(f"\nTotal time spent on {subject}: {total_time:.1f} minutes")


# (f) Display study statistics
def study_statistics():
    if not sessions:
        print("\nNo study sessions available for statistics.")
        return

    total_minutes = 0
    subject_totals = {}

    for session in sessions:
        total_minutes += session["duration"]

        subject = session["subject"]

        if subject in subject_totals:
            subject_totals[subject] += session["duration"]
        else:
            subject_totals[subject] = session["duration"]

    total_hours = total_minutes / 60

    print("\n========== STUDY STATISTICS ==========")

    print(f"Total hours studied overall: {total_hours:.2f} hours")

    print("\nTotal study time per subject:")

    for subject, minutes in subject_totals.items():
        print(f"{subject}: {minutes / 60:.2f} hours")

    weakest_subject = min(subject_totals, key=subject_totals.get)

    print(
        f"\nSubject with the least study time: "
        f"{weakest_subject} "
        f"({subject_totals[weakest_subject]:.1f} minutes)"
    )

    longest_session = max(
        sessions,
        key=lambda session: session["duration"]
    )

    print(
        f"Longest session: {longest_session['subject']} - "
        f"{longest_session['topic']} "
        f"({longest_session['duration']:.1f} minutes)"
    )


# (g) Save sessions to a file
def save_sessions():
    with open("study_log.txt", "w") as file:

        for session in sessions:
            file.write(
                f"{session['subject']}|"
                f"{session['topic']}|"
                f"{session['date']}|"
                f"{session['duration']}\n"
            )

    print("\nStudy sessions saved successfully.")


# (g) Load sessions from the file
def load_sessions():
    try:
        with open("study_log.txt", "r") as file:

            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    session = {
                        "subject": data[0],
                        "topic": data[1],
                        "date": data[2],
                        "duration": float(data[3])
                    }

                    sessions.append(session)

    except FileNotFoundError:
        # This happens when the program is run for the first time
        print("No previous study log found. Starting a new planner.")


# (a) Main menu
def main():

    # Load previously saved sessions when the program starts
    load_sessions()

    while True:

        print("\n====================================")
        print("       SMART STUDY PLANNER")
        print("====================================")
        print("1. Add a study session")
        print("2. View all sessions")
        print("3. Search sessions by subject")
        print("4. View statistics")
        print("5. Save and exit")
        print("====================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_session()

        elif choice == "2":
            view_sessions()

        elif choice == "3":
            subject = input("Enter subject to search: ")
            search_by_subject(subject)

        elif choice == "4":
            study_statistics()

        elif choice == "5":
            save_sessions()
            print("Thank you for using Smart Study Planner.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# (h) Program entry point
if __name__ == "__main__":
    main()