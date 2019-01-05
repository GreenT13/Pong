from pong import PongConstants, PongGlobalVariables


def determineMiddleOfMenuItem(nrOfItems, spaceBetweenItems, sizeOfItem, index):
    """
    Calculate the difference between the middle of the screen and a menu item. We assume there are ``nrOfItems`` shown
    on the screen in total, where each item has the same size (``sizeOfItem``).

    :param nrOfItems: n (must be an integer)
    :param spaceBetweenItems: delta
    :param sizeOfItem: x
    :param index: index of the item inside the menu (0-based).
    :return: float (or int if every given number is an int)
    """

    # We differentiate between even and odd nrOfItems.
    if nrOfItems % 2 == 0:
        return (index - (nrOfItems / 2) + 0.5) * (sizeOfItem + spaceBetweenItems)
    else:
        return (index + 1 - ((nrOfItems + 1) / 2)) * (sizeOfItem + spaceBetweenItems)


def writeTextOnScreen(text, centerX, centerY, color=PongConstants.COLOR_RED, underlineItem=False):
    """
    Draw text on screen, centered around the point (centerX, centerY). Underline text if specified.

    :param text: the text that will be written on the screen.
    :param centerX: the x-coordinate of the middle of the text.
    :param centerY: the y-coordinate of the middle of the text.
    :param color: the color of the text to write.
    :param underlineItem: boolean indication of whether text must be underlined.
    """
    if underlineItem:
        font = PongConstants.FONT_UNDERLINE
    else:
        font = PongConstants.FONT

    renderedText = font.render(text, True, color)
    textRect = renderedText.get_rect()
    textRect.centerx = centerX
    textRect.centery = centerY

    PongGlobalVariables.screen.blit(renderedText, textRect)
