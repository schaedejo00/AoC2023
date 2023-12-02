import Data.Char

main :: IO()
main = do
    contents <- readFile "./D01/input.txt"
    print (solve contents)

solve :: String -> Integer
solve inp = sum (map lineValue (getFileLines inp))

lineValue :: String -> Integer
lineValue line = strToint (leftmostDigit line :  [leftmostDigit (reverse line)])

leftmostDigit :: String -> Char
leftmostDigit (xs:rest) 
                    | isDigit xs = xs
                    | otherwise = leftmostDigit rest

--libs

getFileLines :: String -> [String] 
getFileLines = lines

strToint :: String -> Integer
strToint s = read s :: Integer
