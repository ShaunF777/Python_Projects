"""
🐰 Interactive Python Unit Testing Tutorial 🐰
==============================================

This program provides an interactive tutorial on Python unit testing concepts
based on CS50P Lecture 5. It covers:
- Basic unit testing concepts and why they matter
- Using assert statements for testing  
- Introduction to pytest framework
- Testing functions that return values vs. print
- Organizing tests into folders
- Exception testing with pytest.raises

DEPENDENCIES:
- Python 3.x (built-in)
- pytest (install with: pip install pytest)

NOTE: This tutorial demonstrates concepts but doesn't create separate .py files.
In real practice, you would create:
1. calculator.py - the main program file
2. test_calculator.py - the test file
3. hello.py - example program for string testing
4. test_hello.py - tests for hello function
5. test/ folder with __init__.py for organized testing

If you want to create these files after the tutorial, I can help you generate them!

Author: Interactive Learning Assistant
"""

import time
import random

class UnitTestingTutorial:
    def __init__(self):
        self.name = ""
        self.progress = 0
        
    def slow_print(self, text, delay=1):
        """Print text with a small delay for dramatic effect"""
        print(text)
        time.sleep(delay)
    
    def get_input(self, prompt):
        """Get user input with emoji flair"""
        return input(f"🤔 {prompt}")
    
    def celebrate(self):
        """Celebrate progress with random emojis"""
        celebrations = ["🎉", "🌟", "🚀", "✨", "🎊", "🏆"]
        return random.choice(celebrations)
    
    def introduction(self):
        """Welcome and get to know the user"""
        print("=" * 60)
        print("🐰 Welcome to Peter Rabbit's Unit Testing Adventure! 🐰")
        print("=" * 60)
        
        self.name = self.get_input("What's your name, fellow programmer? ")
        
        print(f"\n🌟 Hello {self.name}! I'm so excited to explore unit testing with you!")
        
        experience = self.get_input(f"Have you done any testing before, {self.name}? (yes/no/a little): ").lower()
        
        if "yes" in experience:
            print(f"🎯 Fantastic {self.name}! Let's polish those testing skills!")
        elif "no" in experience:
            print(f"🌱 Perfect {self.name}! We'll start from the very beginning!")
        else:
            print(f"📚 Great {self.name}! Let's build on what you know!")
            
        self.slow_print("\n🐰 Just like Peter Rabbit needs to test if Mr. McGregor's garden is safe,")
        self.slow_print("we need to test if our code works correctly before sharing it!")
        
        ready = self.get_input(f"\nReady to hop into testing, {self.name}? (press Enter): ")
        print(f"\n{self.celebrate()} Let's begin our adventure!")
    
    def why_unit_testing(self):
        """Explain the importance of unit testing"""
        print("\n" + "=" * 50)
        print("📖 Chapter 1: Why Unit Testing Matters")
        print("=" * 50)
        
        self.slow_print(f"🤔 {self.name}, imagine you're writing a story about the Famous Five...")
        self.slow_print("You'd want to check each chapter makes sense before publishing, right?")
        
        answer = self.get_input("How do you think most programmers test their code? ").lower()
        
        print(f"\n💡 Great thinking, {self.name}!")
        self.slow_print("Many programmers use print() statements to check their code.")
        self.slow_print("But there's a much better way - UNIT TESTING! 🧪")
        
        print("\n🏭 In the programming industry:")
        print("   • Programmers write code to test their own programs")
        print("   • This is more reliable than manual testing")
        print("   • Tests can be run automatically")
        print("   • Tests catch bugs before users see them")
        
        confidence = self.get_input(f"\n{self.name}, on a scale of 1-10, how confident are you about testing? ")
        print(f"\n{self.celebrate()} Thanks for sharing! Let's boost that confidence!")
    
    def basic_assert_concept(self):
        """Introduce assert statements"""
        print("\n" + "=" * 50)
        print("⚡ Chapter 2: The Magic of Assert Statements")
        print("=" * 50)
        
        self.slow_print(f"🎭 {self.name}, let's pretend we have a magical calculator...")
        self.slow_print("We want to test if it correctly squares numbers!")
        
        print("\n📝 Here's our calculator function:")
        print("""
def square(n):
    return n * n
        """)
        
        test_number = self.get_input("What number should we test first? ")
        
        try:
            num = int(test_number)
            expected = num * num
            print(f"\n🧮 If square({num}) works correctly, it should return {expected}")
        except ValueError:
            print(f"\n🙈 Oops! Let's use the number 2 for our example!")
            num, expected = 2, 4
        
        self.slow_print(f"\n✨ Instead of using print() statements, we can use 'assert'!")
        
        print("\n📚 The old way (with print):")
        print(f"""
def test_square():
    if square({num}) != {expected}:
        print("{num} squared was not {expected}")
        """)
        
        print(f"\n🚀 The better way (with assert):")
        print(f"""
def test_square():
    assert square({num}) == {expected}
        """)
        
        understanding = self.get_input(f"\n{self.name}, what do you think 'assert' does? ")
        
        print(f"\n{self.celebrate()} Excellent thinking!")
        self.slow_print("🔍 'assert' tells Python: 'This MUST be true!'")
        self.slow_print("If it's not true, Python raises an AssertionError")
        self.slow_print("If it IS true, the program continues normally")
    
    def demonstrate_assert_failure(self):
        """Show what happens when assertions fail"""
        print("\n" + "=" * 50)
        print("💥 Chapter 3: When Things Go Wrong")
        print("=" * 50)
        
        self.slow_print(f"🐛 {self.name}, let's see what happens when our code has a bug...")
        
        print("\n🔧 Imagine our square function was broken:")
        print("""
def square(n):
    return n + n  # OOPS! Should be n * n
        """)
        
        self.slow_print("Now when we run: assert square(3) == 9")
        self.slow_print("We get: AssertionError!")
        
        bug_experience = self.get_input("Have you ever had a bug that was hard to find? (yes/no): ").lower()
        
        if "yes" in bug_experience:
            print(f"😅 We've all been there, {self.name}! Tests help catch these early!")
        else:
            print(f"🍀 Lucky you, {self.name}! But tests will help prevent future headaches!")
        
        print(f"\n🎯 The beauty of assert statements:")
        print("   • They're simple and clear")
        print("   • They fail fast when something's wrong")
        print("   • They make your code more reliable")
        
        # Interactive demonstration
        print(f"\n🧪 Let's try a quick mental test, {self.name}!")
        test_cases = [
            (2, 4, "correct"),
            (3, 6, "broken - should be 9"),
            (-2, 4, "correct"),
            (0, 0, "correct")
        ]
        
        for num, result, status in test_cases:
            user_guess = self.get_input(f"If square({num}) returns {result}, is this correct? (yes/no): ").lower()
            if ("yes" in user_guess and "correct" in status) or ("no" in user_guess and "broken" in status):
                print(f"   {self.celebrate()} Correct! {status}")
            else:
                print(f"   🤔 Actually, {status}")
    
    def introduce_pytest(self):
        """Introduce the pytest framework"""
        print("\n" + "=" * 50)
        print("🔬 Chapter 4: Meet pytest - Your Testing Sidekick!")
        print("=" * 50)
        
        self.slow_print(f"🎪 {self.name}, remember how the Famous Five had special gadgets?")
        self.slow_print("pytest is like a special gadget for testing!")
        
        print("\n📦 To install pytest:")
        print("   pip install pytest")
        
        installed = self.get_input("Do you have pytest installed? (yes/no/not sure): ").lower()
        
        if "yes" in installed:
            print(f"   {self.celebrate()} Perfect! You're ready to go!")
        else:
            print(f"   📝 No worries! Remember to run 'pip install pytest' later!")
        
        print(f"\n🌟 Why is pytest amazing?")
        print("   • It runs all your tests automatically")
        print("   • It gives detailed error reports")
        print("   • It continues testing even after failures")
        print("   • It's the industry standard")
        
        self.slow_print(f"\n🏃‍♂️ Instead of running: python test_calculator.py")
        self.slow_print("You run: pytest test_calculator.py")
        
        print(f"\n🎨 pytest shows you:")
        print("   • Green dots (.) for passing tests")
        print("   • Red F for failing tests")
        print("   • Detailed error messages")
        
        excitement = self.get_input(f"\n{self.name}, how excited are you to try pytest? (1-10): ")
        print(f"\n{self.celebrate()} That's the spirit! Let's see it in action!")
    
    def pytest_organization(self):
        """Explain how to organize tests with pytest"""
        print("\n" + "=" * 50)
        print("🗂️ Chapter 5: Organizing Your Tests Like Moon-Face's Tree House")
        print("=" * 50)
        
        self.slow_print(f"🌳 {self.name}, remember Moon-Face's organized tree house?")
        self.slow_print("We should organize our tests just as neatly!")
        
        print("\n📋 Instead of one big test function:")
        print("""
def test_square():
    assert square(2) == 4    # positive numbers
    assert square(-2) == 4   # negative numbers  
    assert square(0) == 0    # zero
        """)
        
        print("\n🎯 We can split into focused functions:")
        print("""
def test_positive_numbers():
    assert square(2) == 4
    assert square(3) == 9

def test_negative_numbers():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
        """)
        
        organization_question = self.get_input("Why do you think splitting tests is better? ")
        
        print(f"\n{self.celebrate()} Great insight, {self.name}!")
        print("🎁 Benefits of organized tests:")
        print("   • If one test fails, others still run")
        print("   • Easier to understand what failed")
        print("   • Easier to add new tests")
        print("   • Better error reporting")
        
        categories = self.get_input("\nIf you were testing a 'add' function, what categories would you test? ")
        print(f"\n💡 Great ideas! Common categories include:")
        print("   • Positive numbers")
        print("   • Negative numbers") 
        print("   • Zero")
        print("   • Large numbers")
        print("   • Edge cases")
    
    def testing_exceptions(self):
        """Explain testing for exceptions"""
        print("\n" + "=" * 50)
        print("🚨 Chapter 6: Testing for Trouble (Exception Testing)")
        print("=" * 50)
        
        self.slow_print(f"🎭 {self.name}, what if someone tries to square the word 'rabbit'?")
        self.slow_print("Our function should complain, right?")
        
        print("\n🧪 We can test that errors happen when they should:")
        print("""
import pytest

def test_string_input():
    with pytest.raises(TypeError):
        square("rabbit")
        """)
        
        error_experience = self.get_input("Have you ever wanted your program to give an error? (yes/no): ").lower()
        
        if "yes" in error_experience:
            print(f"   {self.celebrate()} Exactly! Sometimes errors are the right response!")
        else:
            print(f"   🤔 Think of it like Peter Rabbit's mom warning about Mr. McGregor's garden!")
        
        print(f"\n🎪 pytest.raises() is like saying:")
        print("   'I EXPECT this to cause trouble!'")
        print("   'If it doesn't cause trouble, something's wrong!'")
        
        print(f"\n🔍 Common exceptions to test:")
        print("   • TypeError (wrong data type)")
        print("   • ValueError (wrong value)")
        print("   • ZeroDivisionError (dividing by zero)")
        
        which_error = self.get_input("What error would happen if we tried: 10 / 0? ")
        if "zero" in which_error.lower() or "division" in which_error.lower():
            print(f"   {self.celebrate()} Perfect! ZeroDivisionError!")
        else:
            print(f"   💡 That would be a ZeroDivisionError!")
    
    def testing_functions_vs_print(self):
        """Explain the difference between testing functions that return vs print"""
        print("\n" + "=" * 50)
        print("🎭 Chapter 7: The Return vs Print Mystery")
        print("=" * 50)
        
        self.slow_print(f"🕵️ {self.name}, here's a tricky question...")
        self.slow_print("Can we test a function that prints instead of returning?")
        
        print("\n❌ This function is HARD to test:")
        print("""
def greet(name="world"):
    print(f"Hello, {name}")
        """)
        
        print("\n✅ This function is EASY to test:")
        print("""
def greet(name="world"):
    return f"Hello, {name}"
        """)
        
        difference = self.get_input("Can you guess why the second one is easier to test? ")
        
        print(f"\n{self.celebrate()} Great thinking!")
        print("🎯 The key difference:")
        print("   • print() shows something but gives us nothing back")
        print("   • return gives us a value we can check with assert")
        
        print(f"\n🧪 Testing the returnable function:")
        print("""
def test_greet():
    assert greet("Peter") == "Hello, Peter"
    assert greet() == "Hello, world"
        """)
        
        self.slow_print(f"\n📝 Pro tip for {self.name}:")
        self.slow_print("When possible, make functions return values instead of printing!")
        self.slow_print("Then use print() in your main() function!")
        
        design_question = self.get_input("Why might returning be better than printing? ")
        print(f"\n💎 Excellent insight! Functions that return are more flexible!")
    
    def folder_organization(self):
        """Explain organizing tests into folders"""
        print("\n" + "=" * 50)
        print("📁 Chapter 8: The Famous Five's Filing System")
        print("=" * 50)
        
        self.slow_print(f"🗃️ {self.name}, imagine the Famous Five keeping all their clues in one messy pile...")
        self.slow_print("That would be chaos! Same with our tests!")
        
        print("\n🏗️ We can create a special test folder:")
        print("   mkdir test")
        
        print("\n📄 Then put our tests inside:")
        print("   test/test_calculator.py")
        print("   test/test_hello.py")
        print("   test/test_math.py")
        
        print("\n🔑 The magic file - __init__.py:")
        print("   test/__init__.py")
        print("   (This can be empty, but tells pytest this is a test folder)")
        
        organization_style = self.get_input("How do you usually organize your files? ")
        
        print(f"\n{self.celebrate()} Great approach!")
        print("🎯 Running all tests in a folder:")
        print("   pytest test")
        print("   (This runs ALL test files in the test folder!)")
        
        print(f"\n🌟 Benefits of organized testing:")
        print("   • Easy to find specific tests")
        print("   • Can run all tests with one command")
        print("   • Keeps main code folder clean")
        print("   • Professional standard")
        
        scale_question = self.get_input("How many test files do you think a big project might have? ")
        print(f"\n🤯 Big projects can have hundreds or thousands of test files!")
        print(f"   That's why organization matters so much!")
    
    def best_practices_quiz(self):
        """Interactive quiz on best practices"""
        print("\n" + "=" * 50)
        print("🧠 Chapter 9: Peter Rabbit's Testing Wisdom Quiz")
        print("=" * 50)
        
        self.slow_print(f"🎓 Time for a fun quiz, {self.name}!")
        self.slow_print("Let's see what you've learned!")
        
        questions = [
            {
                "question": "Should you test only when your code is broken?",
                "options": ["A) Yes, only test broken code", "B) No, test working code too"],
                "correct": "B",
                "explanation": "We test working code to make sure it STAYS working!"
            },
            {
                "question": "What's better for testing?",
                "options": ["A) Functions that return values", "B) Functions that print"],
                "correct": "A", 
                "explanation": "Return values can be checked with assert!"
            },
            {
                "question": "When should you split tests into multiple functions?",
                "options": ["A) Never", "B) When testing different scenarios"],
                "correct": "B",
                "explanation": "Split tests help identify exactly what failed!"
            },
            {
                "question": "What does pytest.raises() test?",
                "options": ["A) That functions work correctly", "B) That errors happen when expected"],
                "correct": "B",
                "explanation": "Sometimes we WANT errors - like rejecting invalid input!"
            }
        ]
        
        score = 0
        for i, q in enumerate(questions, 1):
            print(f"\n🤔 Question {i}: {q['question']}")
            for option in q['options']:
                print(f"   {option}")
            
            answer = self.get_input("Your answer (A/B): ").upper().strip()
            
            if answer == q['correct']:
                score += 1
                print(f"   {self.celebrate()} Correct!")
            else:
                print(f"   🤔 Not quite - the answer is {q['correct']}")
            print(f"   💡 {q['explanation']}")
        
        print(f"\n🏆 {self.name}, you scored {score}/{len(questions)}!")
        
        if score == len(questions):
            print("   🌟 Perfect! You're a testing master!")
        elif score >= len(questions) // 2:
            print("   🎯 Great job! You've got the important concepts!")
        else:
            print("   📚 Keep practicing - you're on the right track!")
    
    def final_summary(self):
        """Provide a comprehensive summary"""
        print("\n" + "=" * 60)
        print("🎊 Congratulations! Testing Adventure Complete! 🎊")
        print("=" * 60)
        
        print(f"\n🌟 {self.name}, you've learned SO much today!")
        
        print("\n📚 Your Testing Toolkit:")
        print("   1️⃣  Unit Tests - Test small pieces of code")
        print("   2️⃣  assert - Check that something is true")
        print("   3️⃣  pytest - Professional testing framework")
        print("   4️⃣  Test Organization - Split tests into focused functions")
        print("   5️⃣  Exception Testing - Test that errors happen when expected")
        print("   6️⃣  Return vs Print - Return values for easier testing")
        print("   7️⃣  Folder Organization - Keep tests organized and clean")
        
        print(f"\n🔧 Essential Commands to Remember:")
        print("   • pip install pytest")
        print("   • pytest test_filename.py")
        print("   • pytest foldername")
        
        print(f"\n✨ Key Testing Principles:")
        print("   • Test early, test often")
        print("   • Write tests for different scenarios")
        print("   • Make functions return values when possible")
        print("   • Organize tests clearly")
        print("   • Test both success and failure cases")
        
        confidence_after = self.get_input(f"\n{self.name}, how confident do you feel about testing now? (1-10): ")
        
        print(f"\n{self.celebrate()} Fantastic progress!")
        
        next_steps = self.get_input("What would you like to practice first - writing tests or organizing them? ")
        
        print(f"\n🚀 Perfect choice! Remember:")
        print("   • Start small with simple assert statements")
        print("   • Practice makes perfect")
        print("   • Every test you write makes your code stronger")
        
        print(f"\n🐰 Thanks for joining Peter Rabbit's testing adventure, {self.name}!")
        print("   Happy coding and testing! 🌟")
        
        # Offer to create example files
        create_files = self.get_input("\nWould you like me to help you create the example files mentioned in this tutorial? (yes/no): ").lower()
        
        if "yes" in create_files:
            print(f"\n📝 Great! In your next message, ask me to create:")
            print("   • calculator.py and test_calculator.py")
            print("   • hello.py and test_hello.py") 
            print("   • Or any specific testing files you want to practice with!")
        else:
            print(f"\n👍 No problem! You now have all the knowledge to create them yourself!")
        
        print(f"\n🎯 Remember: Good tests lead to great code!")
    
    def run_tutorial(self):
        """Run the complete tutorial"""
        try:
            self.introduction()
            self.why_unit_testing()
            self.basic_assert_concept()
            self.demonstrate_assert_failure()
            self.introduce_pytest()
            self.pytest_organization()
            self.testing_exceptions()
            self.testing_functions_vs_print()
            self.folder_organization()
            self.best_practices_quiz()
            self.final_summary()
            
        except KeyboardInterrupt:
            print(f"\n\n🐰 Thanks for the adventure, {self.name}!")
            print("   Come back anytime to continue learning! 🌟")
        except Exception as e:
            print(f"\n🤔 Oops! Something unexpected happened: {e}")
            print("   But that's okay - debugging is part of programming too! 🐛")

def main():
    """Main function to run the tutorial"""
    print("🎬 Starting Peter Rabbit's Unit Testing Adventure...")
    tutorial = UnitTestingTutorial()
    tutorial.run_tutorial()

if __name__ == "__main__":
    main()