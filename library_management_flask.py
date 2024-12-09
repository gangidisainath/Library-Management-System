from flask import Flask, request, jsonify
from data import books, members
from auth import validate_token

app = Flask(__name__)
@app.before_request
def authenticate():
    if request.endpoint != "status":
        token = request.headers.get("token")
        if not validate_token(token):
            return jsonify({"error": "Unauthorized"}), 401

@app.route("/status", methods=["GET"])
def health():
    return jsonify({"status": "OK"})
@app.route("/books", methods=["GET", "POST"])
def handle_books():
    if request.method == "GET":
        search_query = request.args.get("search", "").lower()
        page = int(request.args.get("page", 1))
        limit = 5
        filtered_books = [
            book for book in books if search_query in book["title"].lower() or search_query in book["author"].lower()
        ]
        paginated_books = filtered_books[(page - 1) * limit : page * limit]
        return jsonify(paginated_books)

    elif request.method == "POST":
        data = request.json
        book_id = len(books) + 1
        new_book = {"id": book_id, "title": data["title"], "author": data["author"]}
        books.append(new_book)
        return jsonify(new_book), 201


@app.route("/books/<int:book_id>", methods=["GET", "PUT", "DELETE"])
def manage_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    
    if request.method == "GET":
        return jsonify(book)

    elif request.method == "PUT":
        data = request.json
        book.update({"title": data["title"], "author": data["author"]})
        return jsonify(book),201

    elif request.method == "DELETE":
        books.remove(book)
        return jsonify({"message": "Book deleted"}), 200

@app.route("/members", methods=["GET", "POST"])
def handle_members():
    if request.method == "GET":
        return jsonify(members)

    elif request.method == "POST":
        data = request.json
        member_id = len(members) + 1
        new_member = {"id": member_id, "name": data["name"], "email": data["email"]}
        members.append(new_member)
        return jsonify(new_member), 201


@app.route("/members/<int:member_id>", methods=["GET", "PUT", "DELETE"])
def manage_member(member_id):
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        return jsonify({"error": "Member not found"}), 404

    if request.method == "GET":
        return jsonify(member)

    elif request.method == "PUT":
        data = request.json
        member.update({"name": data["name"], "email": data["email"]})
        return jsonify(member)

    elif request.method == "DELETE":
        members.remove(member)
        return jsonify({"message": "Member deleted"}), 200


if __name__ == "__main__":
    app.run(debug=False)
