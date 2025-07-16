import socket
import json
import random

class QuizServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.quiz_data = [
            {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is the largest planet in our solar system?", "choices": ["Jupiter", "Saturn", "Mars", "Earth"], "answer": "Jupiter"},
            {"question": "What is the chemical symbol for gold?", "choices": ["Go", "Au", "Ag", "Gd"], "answer": "Au"},
            {"question": "Which country is known as the 'Land of the Rising Sun'?", "choices": ["China", "Japan", "South Korea", "Thailand"], "answer": "Japan"},
            {"question": "What is the largest living species of lizard?", "choices": ["Komodo dragon", "Saltwater crocodile", "Black mamba", "Green anaconda"], "answer": "Komodo dragon"},
            {"question": "What is the world's largest waterfall, by volume of water?", "choices": ["Victoria Falls", "Iguazu Falls", "Niagara Falls", "Angel Falls"], "answer": "Victoria Falls"},
            {"question": "What is the highest mountain peak in the solar system?", "choices": ["Mount Everest", "Olympus Mons", "Mauna Kea", "Denali"], "answer": "Olympus Mons"},
            {"question": "What is the deepest part of the ocean?", "choices": ["Mariana Trench", "Challenger Deep", "Tonga Trench", "Kermadec Trench"], "answer": "Challenger Deep"},
            {"question": "What is the longest river in South America?", "choices": ["Amazon River", "Parana River", "Sao Francisco River", "Magdalena River"], "answer": "Amazon River"},
            {"question": "What is the world's largest desert?", "choices": ["Sahara", "Gobi", "Mojave", "Atacama"], "answer": "Sahara"},
            {"question": "What is the highest temperature ever recorded on Earth?", "choices": ["134°F", "120°F", "110°F", "100°F"], "answer": "134°F"},
            {"question": "What is the lowest temperature ever recorded on Earth?", "choices": ["-128.6°F", "-120°F", "-110°F", "-100°F"], "answer": "-128.6°F"},
            {"question": "What is the world's largest island?", "choices": ["Greenland", "New Guinea", "Borneo", "Iceland"], "answer": "Greenland"},
            {"question": "What is the world's longest mountain range?", "choices": ["Andes", "Himalayas", "Rocky Mountains", "Appalachian Mountains"], "answer": "Andes"},
            {"question": "What is the world's largest waterfall, by width?", "choices": ["Victoria Falls", "Iguazu Falls", "Niagara Falls", "Angel Falls"], "answer": "Victoria Falls"},
            {"question": "What is the world's largest lake?", "choices": ["Caspian Sea", "Lake Superior", "Lake Tanganyika", "Lake Baikal"], "answer": "Caspian Sea"},
            {"question": "What is the world's longest river?", "choices": ["Nile River", "Amazon River", "Yangtze River", "Mississippi River"], "answer": "Nile River"},
            {"question": "What is the world's largest coral reef system?", "choices": ["Great Barrier Reef", "Red Sea Coral Reef", "New Caledonia Barrier Reef", "Belize Barrier Reef"], "answer": "Great Barrier Reef"},
            {"question": "What is the world's largest rainforest?", "choices": ["Amazon Rainforest", "Congo Basin", "Daintree Rainforest", "Valdivian Rainforest"], "answer": "Amazon Rainforest"},
            {"question": "What is the world's largest mammal?", "choices": ["Blue whale", "Fin whale", "Humpback whale", "Sperm whale"], "answer": "Blue whale"}
        ]

    def handle_request(self, client_socket):
        request = client_socket.recv(1024).decode()
        if request == "get_quiz_data":
            random_quiz_data = random.sample(self.quiz_data, 6)
            response = json.dumps(random_quiz_data)
            client_socket.sendall(response.encode())
        else:
            client_socket.sendall("Invalid request".encode())

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print("Server started. Listening for incoming connections...")
        while True:
            client_socket, address = server_socket.accept()
            print("Connected by", address)
            self.handle_request(client_socket)
            client_socket.close()

if __name__ == "__main__":
    server = QuizServer("localhost", 8080)
    server.start_server()
