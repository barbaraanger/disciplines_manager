
def calculate_percentage(approved_count, total_count):
    if total_count == 0:
        return 0
    return (approved_count / total_count) * 100
