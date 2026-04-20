from dataclasses import dataclass, field

from app.game_logic import (
    check_bingo,
    generate_board,
    generate_checklist,
    get_winning_square_ids,
    toggle_item,
    toggle_square,
)
from app.models import BingoLine, BingoSquareData, GameMode, GameState, ScavengerItem


@dataclass
class GameSession:
    """Holds the state for a single game session."""

    game_state: GameState = GameState.START
    game_mode: GameMode = GameMode.BINGO
    board: list[BingoSquareData] = field(default_factory=list)
    winning_line: BingoLine | None = None
    show_bingo_modal: bool = False
    checklist: list[ScavengerItem] = field(default_factory=list)

    @property
    def winning_square_ids(self) -> set[int]:
        return get_winning_square_ids(self.winning_line)

    @property
    def has_bingo(self) -> bool:
        return self.game_state == GameState.BINGO

    @property
    def checked_count(self) -> int:
        return sum(1 for item in self.checklist if item.is_checked)

    @property
    def progress_percent(self) -> int:
        if not self.checklist:
            return 0
        return round(self.checked_count / len(self.checklist) * 100)

    def start_game(self) -> None:
        self.board = generate_board()
        self.winning_line = None
        self.game_state = GameState.PLAYING
        self.game_mode = GameMode.BINGO
        self.show_bingo_modal = False
        self.checklist = []

    def start_scavenger_hunt(self) -> None:
        self.checklist = generate_checklist()
        self.board = []
        self.winning_line = None
        self.game_state = GameState.PLAYING
        self.game_mode = GameMode.SCAVENGER_HUNT
        self.show_bingo_modal = False

    def handle_square_click(self, square_id: int) -> None:
        if self.game_state != GameState.PLAYING:
            return
        self.board = toggle_square(self.board, square_id)

        if self.winning_line is None:
            bingo = check_bingo(self.board)
            if bingo is not None:
                self.winning_line = bingo
                self.game_state = GameState.BINGO
                self.show_bingo_modal = True

    def handle_item_click(self, item_id: int) -> None:
        if self.game_state != GameState.PLAYING:
            return
        self.checklist = toggle_item(self.checklist, item_id)

    def reset_game(self) -> None:
        self.game_state = GameState.START
        self.game_mode = GameMode.BINGO
        self.board = []
        self.winning_line = None
        self.show_bingo_modal = False
        self.checklist = []

    def dismiss_modal(self) -> None:
        self.show_bingo_modal = False
        self.game_state = GameState.PLAYING


# In-memory session store keyed by session ID
_sessions: dict[str, GameSession] = {}


def get_session(session_id: str) -> GameSession:
    """Get or create a game session for the given session ID."""
    if session_id not in _sessions:
        _sessions[session_id] = GameSession()
    return _sessions[session_id]
