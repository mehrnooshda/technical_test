from flask import jsonify
from app.models.ram import RamUsage, RamUsageSchema


def get_list_of_ram(last_n_minutes):
    schema = RamUsageSchema(many=True)
    # results = RamUsage.query.all()
    results = RamUsage.query.order_by(RamUsage.id.desc()).limit(last_n_minutes)
    return jsonify(schema.dump(results))
