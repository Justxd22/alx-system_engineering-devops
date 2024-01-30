#!/usr/bin/env ruby
p = ARGV[0].scan(/\[from:(.*?)\]/).flatten
l = ARGV[0].scan(/\[to:(.*?)\]/).flatten
k = ARGV[0].scan(/\[flags:(.*?)\]/).flatten

puts "#{p.join(', ')}, #{l.join(', ')}, #{k.join(', ')}"
