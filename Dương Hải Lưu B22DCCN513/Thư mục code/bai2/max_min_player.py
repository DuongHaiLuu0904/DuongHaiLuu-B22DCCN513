class max_min:
    def __init__(self):
        self.list_max_min = []
    def add_max_min(self, player):
        self.list_max_min.append(player)
    def show(self):
        print(self.list_max_min)

header_max_min = [
    'thuoc_tinh', 'max_first', 'max_second', 'max_thỉd', 'min_third', 'min_second', 'min_first'
]