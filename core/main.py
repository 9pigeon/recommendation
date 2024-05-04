from flask import Flask, request, jsonify
from model import get_data, find_similar_products

app = Flask(__name__)

product_data = get_data()

# http://127.0.0.1:5000/recommendation?target_fin_prdt_cd=001
@app.route('/recommendation', methods=['GET'])
def get_similar_products():
    target_fin_prdt_cd = request.args.get('target_fin_prdt_cd')
    if target_fin_prdt_cd is None:
        return jsonify({"error": "Missing target_fin_prdt_cd parameter"}), 400

    similar_products = find_similar_products(product_data, target_fin_prdt_cd)

    return jsonify({"similar_products": similar_products})


if __name__ == '__main__':
    app.run(debug=True)
