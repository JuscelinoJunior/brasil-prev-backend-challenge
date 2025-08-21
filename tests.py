from simulator import Property, Impulsivo, Exigente, Cauteloso, Aleatorio, Simulator, History

def test_propertyerty_is_vacant():
    property = Property(position=0, cost=100, rent=50)
    assert property.is_vacant() is True

    player = Impulsivo(name="teste")
    player.buy(property)
    assert property.is_vacant() is False
    assert property.owner == player

def test_impulsivo_always_buys():
    player = Impulsivo(name="impulsivo", balance=500)
    property = Property(position=1, cost=200, rent=50)
    assert player.is_willing_to_buy(property) is True

def test_exigente_only_buys_rent_positive():
    player = Exigente(name="exigente", balance=500)
    property = Property(position=2, cost=200, rent=0)
    assert player.is_willing_to_buy(property) is False
    property.rent = 50
    assert player.is_willing_to_buy(property) is True

def test_cauteloso_needs_minimum_balance_left():
    player = Cauteloso(name="cauteloso", balance=100)
    property = Property(position=3, cost=50, rent=20)
    assert player.is_willing_to_buy(property) is False
    property.cost = 20
    assert player.is_willing_to_buy(property) is True

def test_aleatorio_returns_bool():
    p = Aleatorio(name="aleatorio", balance=200)
    property = Property(position=4, cost=100, rent=20)
    result = p.is_willing_to_buy(property)
    assert isinstance(result, bool)

def test_history_tracks_turns():
    history = History()
    player = Impulsivo(name="teste")
    property = Property(position=0, cost=100, rent=50)

    history.set_current_turn(dice=3, player=player, property=property, action="buy", active_players=[player])
    assert "teste" in history.current_turn
    history.new_turn()
    assert len(history.turns_data) == 1
    assert history.current_turn == {}

def test_simulator_runs():
    sim = Simulator()
    result = sim.simulate()

    assert "vencedor" in result
    assert "jogadores" in result
    assert "quantidade-rodadas" in result
    assert "rodadas" in result

    assert result["vencedor"] in ["impulsivo", "exigente", "cauteloso", "aleatorio"]

    assert set(result["jogadores"]) == {"impulsivo", "exigente", "cauteloso", "aleatorio"}

    assert isinstance(result["rodadas"], list)
