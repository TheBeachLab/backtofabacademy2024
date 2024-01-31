function Link(el)
  --print("Original target:", el.target)
  el.target = string.gsub(el.target, '/md/', '/html/')
  el.target = string.gsub(el.target, "%.md", ".html")
  --print("Modified target:", el.target)
  return el
end