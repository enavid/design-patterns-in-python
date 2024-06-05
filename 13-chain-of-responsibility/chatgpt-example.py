class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            return self._successor.handle(request)
        return None


class AHandler(Handler):
    def handle(self, request):
        if request == 'A':
            return 'Handled by A'
        else:
            return super().handle(request)


class BHandler(Handler):
    def handle(self, request):
        if request == 'B':
            return 'Handled by B'
        else:
            return super().handle(request)


class CHandler(Handler):
    def handle(self, request):
        if request == 'C':
            return 'Handled by C'
        else:
            return super().handle(request)


class DHandler(Handler):
    def handle(self, request):
        if request == 'D':
            return 'Handled by D'
        else:
            return super().handle(request)


def main():
    handler_chain = AHandler(BHandler(CHandler(DHandler())))

    requests = ['A', 'B', 'C', 'D', 'E']

    for request in requests:
        result = handler_chain.handle(request)
        if result:
            print(f'{request}: {result}')
        else:
            print(f'{request}: No handler could handle the request.')


if __name__ == '__main__':
    main()
