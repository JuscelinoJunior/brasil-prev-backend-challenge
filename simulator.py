import random
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any


@dataclass
class Property:
    position: int
    cost: int
    rent: int
    owner: Optional["Player"] = None

    def is_vacant(self) -> bool:
        return self.owner is None


@dataclass
class Player(ABC):
    name: str
    balance: int = 300
    position: int = 0
    properties: List[Property] = field(default_factory=list)

    def move(self, dice_result: int, board: List[Property]) -> None:
        new_position: int = (self.position + dice_result) % len(board)
        if self.position + dice_result >= len(board):
            self.balance += 100
        self.position = new_position

    def buy(self, property: Property) -> None:
        self.balance -= property.cost
        self.properties.append(property)
        property.owner = self

    def rent(self, property: Property) -> None:
        self.balance -= property.rent
        property.owner.balance += property.rent

    @abstractmethod
    def is_willing_to_buy(self, property: Property) -> bool:
        pass

class Impulsivo(Player):
    def is_willing_to_buy(self, property: Property) -> bool:
        return self.balance >= property.cost

class Exigente(Player):
    def is_willing_to_buy(self, property: Property) -> bool:
        return self.balance >= property.cost and property.rent > 0

class Cauteloso(Player):
    def is_willing_to_buy(self, property: Property) -> bool:
        return self.balance >= property.cost and self.balance - property.cost >= 80

class Aleatorio(Player):
    def is_willing_to_buy(self, property: Property) -> bool:
        return self.balance >= property.cost and random.choice([True, False])

@dataclass()
class History:
    turns_data: List[Dict[str, Dict[str, Any]]] = field(default_factory=list)
    current_turn: Dict[str, Dict[str, Any]] = field(default_factory=dict)

    def new_turn(self) -> None:
        if self.current_turn:
            self.turns_data.append(self.current_turn.copy())
        self.current_turn.clear()

    def set_current_turn(self, dice: int, player: Player, property: Property, action: Optional[str], active_players) -> None:
        spend = None

        if action == "buy":
            spend = property.cost
        if action == "rent":
            spend = property.rent

        self.current_turn[player.name] = {
            "dado": dice,
            "propriedade": property.position,
            "propriedade-dono": property.owner.name if property.owner else None,
            "acao": action,
            "gasto": spend,
            "saldos": {p.name: p.balance for p in active_players}
        }

class Simulator:
    def __init__(self):
        self.active_players: List[Player] = [
            Impulsivo(name="impulsivo"),
            Exigente(name="exigente"),
            Cauteloso(name="cauteloso"),
            Aleatorio(name="aleatorio")
        ]
        self.eliminated_players = []
        self.board = [Property(position=i, cost=random.randint(50, 200), rent=random.randint(40, 100)) for i in range(20)]

    def simulate(self):
        turn: int = 0
        simulation_history = History()

        while turn < 1000 and self.active_players:
            simulation_history.new_turn()
            eliminated_players_in_turn: List[Player] = []

            for player in self.active_players:
                dice: int = random.randint(1, 6)
                player.move(dice, self.board)
                property: Property = self.board[player.position]

                if not property.is_vacant():
                    player.rent(property)
                    simulation_history.set_current_turn(dice=dice, player=player, property=property, action="rent", active_players=self.active_players)

                elif player.is_willing_to_buy(property):
                    player.buy(property)
                    simulation_history.set_current_turn(dice=dice, player=player, property=property, action="buy", active_players=self.active_players)

                else:
                    simulation_history.set_current_turn(dice=dice, player=player, property=property, action=None, active_players=self.active_players)

                if player.balance < 0:
                    eliminated_players_in_turn.append(player)
                    for player_property in player.properties:
                        player_property.owner = None
                    player.properties = []

            for eliminated_player in eliminated_players_in_turn:
                self.eliminated_players.append(eliminated_player)
                self.active_players.remove(eliminated_player)

            turn += 1

            if len(self.active_players) == 1:
                break

        priority_map = {name: idx for idx, name in enumerate(["impulsivo", "exigente", "cauteloso", "aleatorio"])}

        if len(self.active_players) == 1:
            winner: Player = self.active_players[0]
        else:
            winner: Player = sorted(self.active_players, key=lambda p: (-p.balance, priority_map[p.name]))[0]

        all_players: List[Player] = self.active_players + self.eliminated_players
        ranking: List[Player] = sorted(all_players, key=lambda p: (-p.balance, priority_map[p.name]))

        return {
            "vencedor": winner.name,
            "jogadores": [player.name for player in ranking],
            "quantidade-rodadas": turn,
            "rodadas": simulation_history.turns_data
        }
