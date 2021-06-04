#include <iostream>
#include <fstream>
#include <SFML/Graphics.hpp>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

int mod ( int a1 ) {
  if ( a1 < 0 ) return -a1;
  return a1;
}

static float  threshold = 2;
static bool   labelsActive = true;
static float  weight [ 11 ] = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
static string parameterNames [ 9 ] = { "CLUMP THK.", "SIZE UNIF.", "SHAPE UNIF.", "MARGINAL ADH.", "SEC. SIZE", "BARE NCL.", "BLAND CHRM.", "NORMAL NCL.", "MITOSES" };
  
class DataPoint {
  int actual; 

  public :

  int data[ 11 ];

  DataPoint() { actual = 0; for ( int i = 0; i < 11; i++ ) { data[ i ] = -1; } }
  DataPoint( const DataPoint& a1 ) { actual = a1.actual; for( int i = 0; i < 11; i++ ) { data[ i ] = a1.data[ i ]; } }

  void AddDPV( int a1 ) { if( actual > 11 ) { return; } data[ actual ] = a1; actual++; }

  void Display () {
      for ( int i = 0; i < 11; i ++ ) {
        cout<<data[ i ]<<" ";
      }
      cout<<endl;
  }
  
  float Distance ( const DataPoint& a1 ) {
    float omega = 0;
    int disc = 0;
    if( data[ 0 ] != -1 && a1.data[ 0 ] != -1 && data[ 0 ] != a1.data[ 0 ] ) { omega = 1; disc = 1; }
    for ( int i = 1; i < 11; i++ ) {
      if( data[ i ] < 0 || a1.data[ i ] < 0 ) { continue; }
      
      omega += weight[ i ] * mod( data[ i ] - a1.data[ i ] );
      
      if( data[ i ] - a1.data[ i ] != 0 ) {
        disc++;
      }
      
    }
    if( disc != 0 ) {
      omega /= disc;
    } else {
      return 0;
    }
    return omega;
  }

};

int main() {

  int delta;
  
  vector<DataPoint> core;
  
  sf::Font font;
  if ( !font.loadFromFile("OM.ttf") ) {
      return 1;
  }
  
  ifstream in("../modified2");
  
  for( int i = 0; !in.fail(); i++ ) {
    DataPoint delta0 = DataPoint();
    for( int j = 0; j < 11 && !cin.fail(); j++ ) {
      in>>delta;
      delta0.AddDPV( delta );
    }
    if( !in.fail() ) {
      core.push_back( delta0 );
    }
  }
  
  cout<<"PLEASE INPUT FILTER PARAMETERS ( -1 FOR ANY ) : \n";

  DataPoint deltaI;
    
  for( int i = 0; i < 11; i++ ) {
    cin>>delta;
    deltaI.AddDPV( delta );
  }
  
  bool found0 = false;
  
  for( int i = 0; i < core.size(); i++ ) {
    if( deltaI.Distance( core[ i ] ) == 0 ) {
      found0 = true;
      if ( deltaI.data[ 0 ] != -1 ) deltaI = core[ i ];
      break;
    }
  }
  
  vector<DataPoint> display;
  vector<DataPoint> similar;
    
  if( found0 ) {
  
    for( int i = 0; i < core.size(); i++ ) {
      if( deltaI.Distance( core[ i ] ) == 0 ) {
        display.push_back( core[ i ] );
      } else {
        if( deltaI.Distance( core[ i ] ) <= threshold ) {
          similar.push_back( core[ i ] );
        }
      }
    }
    
    cout<<"FOUND "<<display.size()<<" EXACT MATCHES : \n";
    
    for( int i = 0; i < display.size(); i++ ) {
      display[ i ].Display();
    }
    
    sf::RenderWindow window( sf::VideoMode( 800, 450 ), "Data Display" );
    
    sf::RectangleShape line; 
    sf::Text id;
    sf::Text cls;
    sf::Text pLabel;
  
    id.setFont( font ); cls.setFont( font ); pLabel.setFont( font );
    id.setCharacterSize( 20 ); cls.setCharacterSize( 20 ); pLabel.setCharacterSize( 12 );
    id.move( 10, 10 ); cls.move( 10, 30 );

    id.setString( "ID : " + to_string ( display[ display.size() - 1 ].data[ 0 ] ) );
    cls.setString( ( display[ display.size() - 1 ].data[ 11 ] == 2 ? "CLASS : BENIGN" : "CLASS : MALIGNANT" ) );

    while ( window.isOpen() ) {
    
      sf::Event event;
      while (window.pollEvent(event))
      {
          if (event.type == sf::Event::Closed)
              window.close();
      }
        
      window.clear();
      
      //for( int i = 1; i < 11; i++ ) { display[ display.size() - 1 ].data[ i ] = 5; }
      
      for ( int i = 1, ds = display.size() - 1; i < 11; i++ ) {
        line = sf::RectangleShape( sf::Vector2f( 20, 2.5f ) );

        pLabel.setPosition ( 400 + ( int )( 20 * ( display[ ds ].data[ i ] + 3 ) * cos ( ( 2 * M_PI / 9 ) * i ) ) - 30, 225 + ( int )( 20 * ( display[ ds ].data[ i ] + 3 ) * sin ( ( 2 * M_PI / 9 ) * i ) ) );
        pLabel.setString( parameterNames[ i - 1 ] );

        line.move( 400, 225 );
        line.setScale ( display[ ds ].data[ i ] + 1, 1 );
        line.rotate( 40 * i );
        
        if( labelsActive ) window.draw ( pLabel );
        window.draw ( line );
      }
      
      window.draw( id );
      window.draw( cls );
      window.display();
    }

    window.close();
    
    cout<<"\n";
  
  } else {
  
    cout<<"NO RECORDS MATCH QUERY!\n";
  }
  
  cout<<"FOUND "<<similar.size()<<" SIMILAR CASES @ " << threshold << " THRESHOLD. \n";
    
  if ( similar.size() != 0 ) {
    cout<<"DISPLAY SIMILAR CASES ? ( Y / N ) : \n";
    char deltaC;
    
    while( deltaC != 'Y' && deltaC != 'y' && deltaC != 'n' && deltaC != 'N' ) {
      cin>>deltaC;
    }
    
    if( deltaC == 'Y' || deltaC == 'y' ) {
      for( int i = 0; i < similar.size(); i++ ) {
        similar[ i ].Display();
      }
    }
  }
}  

