import svgwrite

def generate_barcode(barcode):
    svg_document = svgwrite.Drawing(filename = "test-svgwrite.svg",
                                    size = ("800px", "600px"))

    svg_document.add(svg_document.rect(insert = (0, 0),
                                       size = ("200px", "100px"),
                                       stroke_width = "1",
                                       stroke = "black",
                                       fill = "rgb(255,255,0)"))

    svg_document.add(svg_document.text(barcode,
                                       insert = (210, 110)))
    return svg_document.tostring()
