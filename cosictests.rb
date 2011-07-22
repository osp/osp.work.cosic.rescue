#!/usr/bin/ruby

puts "COSIC Logo Tests"
puts "	-> LaTeX (markdown2pdf)"
puts "	-> Context"
puts "	-> ODT"

testing = ARGV[0]
fullpath = File.expand_path(testing)
dir = File.dirname(fullpath)

mkd = "#{dir}/tests/#{testing}.mkd"

markdown = "![#{fullpath}](#{fullpath})"

if File.directory?("#{dir}/tests") 
	mkfile = File.open("#{mkd}", "w")
	mkfile.puts markdown
	mkfile.close
else
	Dir.mkdir("#{dir}/tests")
	mkfile = File.open("#{mkd}", "w")
	mkfile.puts markdown
	mkfile.close
end

puts "\nLaTeX"
#puts "  -> Generating the LaTeX document (markdown2pdf)"
#latex = Thread.new do
#	%x[markdown2pdf -o #{mkd}-latex.pdf #{mkd}]
#end
#latex.join

puts "  -> Generating LaTeX with Pandoc"
latex = Thread.new do
	%x[pandoc -o #{mkd}-latex.tex #{mkd} -s]
end
latex.join

puts "  -> Generating LaTeX DVI file"
latex = Thread.new do
	Dir.chdir("#{dir}/tests")
	%x[latex #{mkd}-latex.tex]
end
latex.join

puts "  -> Converting DVI to PostScript"
latex = Thread.new do
	Dir.chdir("#{dir}/tests")
	%x[dvips #{mkd}-latex.dvi]
end
latex.join

puts "  -> Converting PostScript file to PDF"
latex = Thread.new do
	Dir.chdir("#{dir}/tests")
	%x[ps2pdf #{mkd}-latex.ps]
end
latex.join

puts "  -> Viewing the LaTeX PDF"
viewer = Thread.new do 
	%x[evince #{mkd}-latex.pdf]
end
viewer.join

puts "\nContext"
puts "  -> Converting to Context..."
context = Thread.new do
	%x[pandoc -t context -o #{mkd}-context.tex #{mkd} -s]
end
context.join

puts "  -> Running Context to generate PDF"
context = Thread.new do
	Dir.chdir("#{dir}/tests")
	%x[context #{mkd}-context.tex]
#	File.delete("#{dir}/m_k_i_v_#{File.basename(testing, '.eps')}.pdf")
end
context.join

puts "  -> Viewing the Context PDF"
viewer = Thread.new do
	%x[evince #{mkd}-context.pdf]
end
viewer.join

puts "\nODT"
puts "  -> Generating the ODT"
odt = Thread.new do
	%x[pandoc -o #{mkd}.odt #{mkd}]
end
odt.join

puts "  -> Opening the ODT"
viewer = Thread.new do
	%x[libreoffice #{mkd}.odt]
end
viewer.join
