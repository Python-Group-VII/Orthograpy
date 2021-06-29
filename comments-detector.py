#!/usr/bin/env python3.9

def comments_detector(file):
    comments = []
    if not(isinstance(file, list) and all(isinstance(line, str) for line in file)):
        raise TypeError("Only string lists are allowed")
    else:
        for line in file:
            index = line.find('#')
            if index >= 0:
                comments.append(line[index + 1:])
    return (comments)
