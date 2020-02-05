import React, { useState } from "react";
import { StyleSheet, Text, View, Button } from "react-native";

export default function App() {
  const [outputText, setOutputText] = useState("Ola mundo!");
  return (
    <View style={styles.container}>
      <Text>{outputText}</Text>
      <Button
        class="btn-savio"
        title="mudar texto"
        onPress={() => setOutputText("Texto foi modificado com sucesso")}
      ></Button>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "orange"
  }
});
