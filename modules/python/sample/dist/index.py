def execute(data):
    return {
        "success": True,
        "message": f"Hello {data.get('name', 'World')}!",
        "computation": data.get("value", 0) * 2
    }