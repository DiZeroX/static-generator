class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None) -> None:
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
    
  def to_html(self):
    raise NotImplementedError("to_html method not implemented")
  
  def props_to_html(self):
    if self.props is None:
      return ""
    html_string = ""
    for prop in self.props:
      html_string += f' {prop}="{self.props[prop]}"'
    return html_string
      
  def __repr__(self):
    return f"\nHTMLNode(Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props})\n"