function addSubheader(parent, text) {
    return parent.append("div")
        .attr("class", "subheader")
        .style("width", width - padding.horizontal * 2)
        .style("color", color.subdued)
        .text(text)
}

function addHeader(parent, text) {
    return parent.append("div")
        .attr("class", "header")
        .style("width", width - padding.horizontal * 2)
        .style("word-wrap", "break-word")
        .style("color", color.ink)
        .text(text)
}