def summarize_by_category(expenses):
    """Return dictionary with category totals."""
    summary = {}

    for expense in expenses:
        if expense.category not in summary:
            summary[expense.category] = 0.0
        summary[expense.category] += expense.amount

    return summary