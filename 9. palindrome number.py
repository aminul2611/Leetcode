class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10
if __name__ == "__main__":
    sol = Solution()

    print(" exit")
    while True: 
        user_input = input("Enter an interger: ")

        if user_input == 'exit':
            print("Goodbye!")
            break
    
        try:
            number = int(user_input)

            is_pali = sol.isPalindrome(number)

            print(f"Input: x = {number}")
            print(f"Output: {str(is_pali).lower()}")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


