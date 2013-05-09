from code128 import Code128
import svgwrite

def generate_barcode(barcode):
    code = Code128()
    binary = code.makeCode(barcode)
    if binary:
        svg_document = svgwrite.Drawing(filename = "test-svgwrite.svg", size = ("800px", "600px"))
        start_x = 50
        start_y = 50
        bar_size = ("2px", "70px")
        x = 0

        for b in binary:
            if b == '1':
                svg_document.add(svg_document.rect(insert = (start_x + x, start_y), size = bar_size, fill = "rgb(0,0,0)"))
            else:
                svg_document.add(svg_document.rect(insert = (start_x + x, start_y), size = bar_size, fill = "rgb(255,255,255)"))
            x += 2
        svg_document.add(svg_document.text(barcode, insert = (start_x + 50, start_y + 90)))
        return svg_document.tostring()
    else:
        return None
