class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''
    MAX_PLAYER = 4
    MIN_PLAYER = 2
    def __init__(self,players):
        self.players = players
        self.deck = None
        self.winner = None

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        pass

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        pass

    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        pass

    def add_player(self):
        '''Thêm một người chơi mới'''
        pass

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        pass

    def deal_card(self):
        '''Chia bài cho người chơi'''
        pass

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        pass
    