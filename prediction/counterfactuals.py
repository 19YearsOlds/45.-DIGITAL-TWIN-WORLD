def compare(baseline, intervention):
    return [
        {k: intervention[i][k] - baseline[i][k] for k in baseline[i]}
        for i in range(len(baseline))
    ]