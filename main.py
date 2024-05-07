from flask import Flask, request, jsonify
# from model import get_data, find_similar_products
from parsing_prototype import get_recommendations

app = Flask(__name__)



# http://127.0.0.1:5000/recommendation?target_fin_prdt_cd=001&rownum=5
@app.route('/recommendation', methods=['GET'])
def get_similar_products():
    target_fin_prdt_cd = request.args.get('target_fin_prdt_cd')
    rownum = request.args.get('rownum')
    type = request.args.get('type')
    if target_fin_prdt_cd is None:
        return jsonify({"error": "Missing target_fin_prdt_cd parameter"}), 400

    similar_products = get_recommendations(target_fin_prdt_cd, rownum, type)

    return jsonify({"similar_products": similar_products})


if __name__ == '__main__':
    app.run(debug=True)
