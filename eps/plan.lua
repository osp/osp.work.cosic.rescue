-- arrange.plan
-- A lua plan for podofo-impose that arranges pdf pages onto a bigger page
-- Similar to Imagemagick montage command

-- 1mm is 2.83464567pt
mm = 2.83464567

-- The size of our target document. Here: an A3
PageWidth = 297 * mm
PageHeight = 420 * mm

-- Sets the margins
MarginTop = 40
MarginRight = 40
MarginBottom = 40
MarginLeft = 40

-- Effective Width and Height
AreaWidth = PageWidth - MarginRight - MarginLeft
AreaHeight = PageHeight - MarginTop - MarginBottom

-- Computes the number of columns and rows
cols = math.floor(AreaWidth / SourceWidth)
rows = math.floor(AreaHeight / SourceHeight)
itemsPerPage = cols * rows

-- Records
currentSourcePage = 1
while currentSourcePage <= PageCount
do
    -- the current column
    currentCol = (currentSourcePage - 1) % cols
    -- the current x position
    x = MarginLeft + (SourceWidth * currentCol)
    
    -- the current row
    currentRow = math.floor((currentSourcePage - 1) / cols) % rows
    -- the current y position
    y = MarginTop + (SourceHeight * currentRow)

    -- the current page
    currentTargetPage = math.ceil(currentSourcePage / itemsPerPage)

    -- PushRecord(sourcepage, targetpage, rotation, x, y)
    PushRecord(currentSourcePage, currentTargetPage, 0, x, y)

    currentSourcePage = currentSourcePage + 1
end

-- vim:ft=lua:
