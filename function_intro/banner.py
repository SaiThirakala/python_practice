def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Print a string centered with ** on both sides

    :param text: The string to be centered and printed.
        An asterisk (*) will result in a row of asterisks of
        length screen_width being printed.
        The default will print a blank line with ** on both sides.
    :param screen_width: The overall width to print within (including
        the 4 spaces allocated for the ** on both sides)
    :raises ValueError: if the supplied string is longer than the
        screen_width.
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*", 60)
banner_text("Consider marketing without any segmentation", 60)
banner_text("Consider marketing without any segmentation", 60)
banner_text("Consider marketing without any segmentation", 60)
banner_text(screen_width=60)
banner_text("Consider marketing without any segmentation", 60)
banner_text("Consider marketing without any segmentation", 60)
banner_text("Consider marketing without any segmentation", 60)
banner_text("*", 60)