#!/usr/bin/env python3

import os
import random
from socketserver import ThreadingTCPServer, StreamRequestHandler

FLAG = "FLAG{math_2.0_super_solver}"

class MathLogicChallengeHandler(StreamRequestHandler):
    def handle(self):
        self.wfile.write(b'Welcome to the Math and Logic Challenge!\n')
        self.wfile.write(b'Solve 10 questions to get the flag.\n')

        questions_solved = 0

        while questions_solved < 10:
            question, answer = self.generate_question()
            self.wfile.write(f"Question {questions_solved + 1}: {question}\n".encode('utf-8'))
            user_answer = self.rfile.readline().decode('utf-8').strip()

            try:
                user_answer = int(user_answer)
            except ValueError:
                self.wfile.write(b'Invalid input. Please enter an integer.\n')
                continue

            if user_answer == answer:
                questions_solved += 1
                self.wfile.write(b'Correct!\n')
            else:
                self.wfile.write(b'Incorrect. Try again.\n')

        self.wfile.write(f"Congratulations! Here is your flag: {FLAG}\n".encode('utf-8'))

    def generate_question(self):
        operations = [
            ('add', '+', lambda a, b: a + b),
            ('subtract', '-', lambda a, b: a - b),
            ('multiply', '*', lambda a, b: a * b),
            ('xor', 'XOR', lambda a, b: a ^ b)
        ]
        operation, symbol, func = random.choice(operations)

        a = random.randint(1, 100)
        b = random.randint(1, 100)

        question_formats = [
            f"What is the result when you {operation} {a} and {b}?",
            f"Calculate: {a} {symbol} {b}",
            f"Find the answer to {a} {operation}ed by {b}",
            f"Compute the following: {a} {operation.upper()} {b}"
        ]

        question = random.choice(question_formats)
        answer = func(a, b)

        return question, answer

class ThreadedMathLogicChallengeServer(ThreadingTCPServer):
    def __init__(self, server_address, handler_class=MathLogicChallengeHandler):
        ThreadingTCPServer.__init__(self, server_address, handler_class)

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 1336
    server = ThreadedMathLogicChallengeServer((HOST, PORT))
    server.allow_reuse_address = True

    print(f"Server running on {HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.shutdown()
