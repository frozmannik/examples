        # Only 2 decimal places, anything else doesn't make sense
        for key in result.keys():
            for i in result[key]:
                result[key][i] = Decimal(result[key][i]).quantize(TWOPLACES)

        try:
            max = 0
            count = 0
            index = 0
            for item in self.meal_set.select_related():
                if item.get_nutritional_values()['energy'] > max:
                    max = item.get_nutritional_values()['energy']
                    index = count
                count+=1

            result['percent']['dailySugar'] = round(result['total']['carbohydrates_sugar'] / result['total']['carbohydrates'] * result['percent']['carbohydrates'] , 2)

            if result['percent']['dailySugar'] > 10 and result['percent']['dailySugar'] < 15:
                result['advice'] = "You need slightly decrease your sugar intake in {} meal.".format(index+1)
            elif result['percent']['dailySugar'] > 15:
                result['advice'] = "You need decrease your sugar intake. Try to get less sugar in {} meal".format(index+1)
            else:
                result['advice'] = " You are doing well"

        except error as e:
            print(e)

        return result
