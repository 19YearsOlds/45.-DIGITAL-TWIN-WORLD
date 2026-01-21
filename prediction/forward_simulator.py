def run(world, systems, coupler, years):
    history = []
    for _ in range(years):
        coupler.step(*systems)
        history.append({
            "temp": systems[0].temperature,
            "gdp": systems[1].gdp,
            "pop": systems[2].population
        })
    return history