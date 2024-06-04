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
  
class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None) -> None:
    super().__init__(tag, None, children, props)
    
  def to_html(self):
    if self.tag is None:
      raise ValueError("Invalid HTML: missing tag")
    if self.children is None:
      raise ValueError("Invalid HTML: ParentNode needs children")
    children_values = ""
    for child in self.children:
      children_values += child.to_html()
    return f'<{self.tag}{self.props_to_html()}>{children_values}</{self.tag}>'

  def __repr__(self):
      return f"\nParentNode({self.tag}, children: {self.children}, {self.props})\n"

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None) -> None:
    super().__init__(tag=tag, value=value, props=props)
  
  def to_html(self):
    if self.value is None:
      raise ValueError("Invalid HTML: missing value")
    if self.tag is None:
      return self.value
    
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
  def __repr__(self):
    return f"\nLeafNode({self.tag}, {self.value}, {self.props})\n"
    