from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

local_host_numbers = [1, 2, 3, 5, 7, 8, 9, 11, 13, 15, 17, 19, 21, 23]

def fetch_url(url, results):
    try:
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            data = response.json()
            if 'numbers' in data:
                results.extend(data['numbers'])
    except Exception as e:
        pass

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    results = local_host_numbers.copy()

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    merged_numbers = sorted(list(set(results)))

    return jsonify({'numbers': merged_numbers})

@app.route('/prime-numbers', methods=['GET'])
def get_prime_numbers():
    urls = request.args.getlist('url')
    results = []

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    prime_numbers = [num for num in results if is_prime(num)]

    return jsonify({'prime_numbers': prime_numbers})

@app.route('/fibo-numbers', methods=['GET'])
def get_fibo_numbers():
    urls = request.args.getlist('url')
    results = []

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    fibo_numbers = [num for num in results if is_fibo(num)]

    return jsonify({'fibo_numbers': fibo_numbers})

@app.route('/rand-numbers', methods=['GET'])
def get_rand_numbers():
    urls = request.args.getlist('url')
    results = local_host_numbers.copy()

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    rand_numbers = sorted(list(set(results)))

    return jsonify({'rand_numbers': rand_numbers})

@app.route('/odd-numbers', methods=['GET'])
def get_odd_numbers():
    urls = request.args.getlist('url')
    results = local_host_numbers.copy()

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    odd_numbers = [num for num in results if num % 2 != 0]

    return jsonify({'odd_numbers': odd_numbers})

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibo(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

if __name__ == '__main__':
    app.run(debug=True, port=8008)
