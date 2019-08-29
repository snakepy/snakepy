/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React from 'react';
import { Platform, StyleSheet, Text, View } from 'react-native';
import { ApolloClient } from 'apollo-client';
import { ApolloProvider, Query } from 'react-apollo';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { HttpLink } from 'apollo-link-http';
import gql from "graphql-tag";
import * as q from "./queries/queries";

const cache = new InMemoryCache();

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#FFF',
  },
});

const apiurl = Platform.select({
  android: "http://10.0.2.2:8000/graphql",
  ios: "http://localhost:8000/graphql",
});

// Create the client as outlined in the setup guide
const client = new ApolloClient({
  cache,
  link: new HttpLink({
    uri: apiurl,
  }),
});


const SnakePy = () => (
  <View style={styles.container}>
    <Text>
      <Query query={q.queries} >
        {({ loading: loadingOne, erroro, data: datao }) => {
          if (loadingOne) return "loading";
          return(
            <Query query={gql("query { " + datao['__type']['fields'].map(function(x) {
              return([
                x['name'],
                x['type']['ofType']['fields'].map(
                  function(y) { return y['name']}
                ).join(' ')
              ].join(' { ') + ' } ')
            }).join(' ') + " } " )} >
              {({ loading, error, data }) => {
                if (loadingOne || loading) return "loading";      
                return (
                  JSON.stringify(data, null, 1)
                );
              }}
            </Query>
          );
        }}
      </Query>
    </Text>
  </View>
);

const App = () => (
  <ApolloProvider client={client}>
    <SnakePy />
  </ApolloProvider>
);

export default App



// /**
//  * Sample React Native App
//  * https://github.com/facebook/react-native
//  *
//  * @format
//  * @flow
//  */

// import React, {Component} from 'react';
// import {Platform, StyleSheet, Text, View} from 'react-native';

// const instructions = Platform.select({
//   ios: 'Press Cmd+R to reload,\n' + 'Cmd+D or shake for dev menu',
//   android:
//     'Double tap R on your keyboard to reload,\n' +
//     'Shake or press menu button for dev menu',
// });

// type Props = {};
// export default class App extends Component<Props> {
//   render() {
//     return (
//       <View style={styles.container}>
//         <Text style={styles.welcome}>Welcome to React Native!</Text>
//         <Text style={styles.instructions}>To get started, edit App.js</Text>
//         <Text style={styles.instructions}>{instructions}</Text>
//       </View>
//     );
//   }
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     justifyContent: 'center',
//     alignItems: 'center',
//     backgroundColor: '#F5FCFF',
//   },
//   welcome: {
//     fontSize: 20,
//     textAlign: 'center',
//     margin: 10,
//   },
//   instructions: {
//     textAlign: 'center',
//     color: '#333333',
//     marginBottom: 5,
//   },
// });
