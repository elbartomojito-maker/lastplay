# Last Played Resume Plugin

class LastPlayed:
    def __init__(self):
        self.last_played = None

    def play(self, item):
        self.last_played = item
        print(f'Playing: {item}')

    def resume(self):
        if self.last_played:
            print(f'Resuming: {self.last_played}')
        else:
            print('No item to resume.')

# Example usage
if __name__ == '__main__':
    lp = LastPlayed()
    lp.play('Song A')
    lp.resume()
    lp.play('Song B')
    lp.resume()