from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# Criação do diagrama de classes Manter Cliente para draw.io (formato XML compatível)
def create_class_diagram_drawio():
    diagram = Element("mxfile", host="app.diagrams.net", version="20.8.3")
    diagram_root = SubElement(diagram, "diagram", name="Manter Cliente")
    mxGraphModel = SubElement(diagram_root, "mxGraphModel")
    root = SubElement(mxGraphModel, "root")

    # Elemento base
    SubElement(root, "mxCell", id="0")
    SubElement(root, "mxCell", id="1", parent="0")

    # Função auxiliar
    def add_class(id_, name, attributes, methods, x, y):
        cell = SubElement(root, "mxCell", id=id_, value=f"&lt;b&gt;{name}&lt;/b&gt;&lt;br/&gt;{'<br/>'.join(attributes)}&lt;br/&gt;&lt;hr/&gt;{'<br/>'.join(methods)}", style="shape=rectangle;whiteSpace=wrap;html=1;rounded=1;strokeColor=#000000;fillColor=#dae8fc;", vertex="1", parent="1")
        geometry = SubElement(cell, "mxGeometry", x=str(x), y=str(y), width="160", height="140", as_="geometry")

    # Classes
    add_class("2", "Cliente", ["-id:int", "-nome:string", "-data_nasc:date", "-contato:Contato", "-endereco:Endereco"],
              ["+cadastrar()", "+alterar()", "+excluir()", "+consultar()"], 40, 40)
    add_class("3", "Contato", ["-id:int", "-telefone:string", "-email:string", "-whatsapp:string"], [], 300, 40)
    add_class("4", "Endereco", ["-id:int", "-rua:string", "-numero:string", "-bairro:string", "-cidade:string", "-estado:string"], [], 300, 220)
    add_class("5", "ClienteController", [], ["+salvarCliente()", "+editarCliente()", "+removerCliente()", "+buscarCliente()"], 560, 40)
    add_class("6", "ClienteBoundary", [], ["+exibirFormulario()", "+mostrarCliente()", "+solicitarDadosCliente()", "+mostrarMensagem()"], 560, 220)

    # Relacionamentos (linhas)
    def add_edge(id_, source, target, label):
        edge = SubElement(root, "mxCell", id=id_, value=label, edge="1", parent="1", source=source, target=target, style="endArrow=classic;html=1;strokeColor=#000000;")
        SubElement(edge, "mxGeometry", relative="1", as_="geometry")

    add_edge("10", "2", "3", "possui")
    add_edge("11", "2", "4", "reside em")
    add_edge("12", "6", "5", "usa")
    add_edge("13", "5", "2", "manipula")

    xml_str = minidom.parseString(tostring(diagram)).toprettyxml(indent="  ")
    return xml_str

xml_output = create_class_diagram_drawio()

# Salvar o arquivo
path = "/mnt/data/diagrama_classe_manter_cliente.drawio"
with open(path, "w", encoding="utf-8") as f:
    f.write(xml_output)

path
