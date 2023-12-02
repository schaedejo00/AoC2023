import Data.Char
import Data.List
import Data.Maybe (isJust, fromMaybe)

main :: IO()
main = do
    contents <- readFile "./D01/input.txt"
    print (solve contents)

solve :: String -> Integer
solve inp = sum (map lineValue (getFileLines inp))

lineValue :: String -> Integer
lineValue line = strToint (leftmostDigit line :  [rightmostDigit line])

leftmostDigit :: String -> Char
leftmostDigit (xs:rest) 
                    | isDigit xs = xs
                    | isDigit token = token 
                    | otherwise = leftmostDigit rest
                    where 
                        token = textToDigit (take 5 (xs:rest)) numbers
                        numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
                    

rightmostDigit :: String -> Char
rightmostDigit str 
                    | isDigit (last str) = last str
                    | isDigit token = token 
                    | otherwise = rightmostDigit (init str)
                    where 
                        token = textToDigit (take 5 (reverse str)) numbers
                        numbers = map reverse ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

textToDigit :: String -> [String] -> Char
textToDigit str numbers            
                | length str < 3 = ' '
                | isJust token = intToDigit (fromMaybe 0 token + 1)
                | otherwise = textToDigit (init str) numbers
                where 
                        token = elemIndex str numbers
                        


--libs

getFileLines :: String -> [String] 
getFileLines = lines

strToint :: String -> Integer
strToint s = read s :: Integer

lastN :: Int -> [a] -> [a]
lastN n xs = drop (length xs - n) xs