def prepare_boards(lengths, needed):
    sorted_lengths=sorted(lengths)
    selected_lengths=sorted_lengths
    total_selected_length=sum(selected_lengths)
    return (lengths, sorted_lengths, selected_lengths, total_selected_length)